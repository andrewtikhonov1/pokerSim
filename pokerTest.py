import gspread
import csv
import time
from oauth2client.service_account import ServiceAccountCredentials
from gspread_formatting import *

credentials_file = 'credentials.json'
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
gc = gspread.authorize(credentials)
spreadsheet_id = '1PvgWVmantT0DIwMTZ0R-NfihEtwRV4zgKg2bOPoY-lE'

worksheet_title = 'Current Session'
currentSession = gc.open_by_key(spreadsheet_id).worksheet(worksheet_title)

worksheet_title = 'Actual Freqs'
actualFreqs = gc.open_by_key(spreadsheet_id).worksheet(worksheet_title)

worksheet_title = 'Expected Freqs'
expectedFreqs = gc.open_by_key(spreadsheet_id).worksheet(worksheet_title)

hands = [
    ["AA", "AKs", "AQs", "AJs", "ATs", "A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s"],
    ["AKo", "KK", "KQs", "KJs", "KTs", "K9s", "K8s", "K7s", "K6s", "K5s", "K4s", "K3s", "K2s"],
    ["AQo", "KQo", "QQ", "QJs", "QTs", "Q9s", "Q8s", "Q7s", "Q6s", "Q5s", "Q4s", "Q3s", "Q2s"],
    ["AJo", "KJo", "QJo", "JJ", "JTs", "J9s", "J8s", "J7s", "J6s", "J5s", "J4s", "J3s", "J2s"],
    ["ATo", "KTo", "QTo", "JTo", "TT", "T9s", "T8s", "T7s", "T6s", "T5s", "T4s", "T3s", "T2s"],
    ["A9o", "K9o", "Q9o", "J9o", "T9o", "99", "98s", "97s", "96s", "95s", "94s", "93s", "92s"],
    ["A8o", "K8o", "Q8o", "J8o", "T8o", "98o", "88", "87s", "86s", "85s", "84s", "83s", "82s"],
    ["A7o", "K7o", "Q7o", "J7o", "T7o", "97o", "87o", "77", "76s", "75s", "74s", "73s", "72s"],
    ["A6o", "K6o", "Q6o", "J6o", "T6o", "96o", "86o", "76o", "66", "65s", "64s", "63s", "62s"],
    ["A5o", "K5o", "Q5o", "J5o", "T5o", "95o", "85o", "75o", "65o", "55", "54s", "53s", "52s"],
    ["A4o", "K4o", "Q4o", "J4o", "T4o", "94o", "84o", "74o", "64o", "54o", "44", "43s", "42s"],
    ["A3o", "K3o", "Q3o", "J3o", "T3o", "93o", "83o", "73o", "63o", "53o", "43o", "33", "32s"],
    ["A2o", "K2o", "Q2o", "J2o", "T2o", "92o", "82o", "72o", "62o", "52o", "42o", "32o", "22"]
]

exp_freqs = [[0 for _ in range(13)] for _ in range(13)]
for i in range(13):
    for j in range(13):
        if (i == j):
            exp_freqs[i][j] = 6/1326
        if (i < j):
            exp_freqs[i][j] = 4/1326
        if (i > j):
            exp_freqs[i][j] = 12/1326

expectedFreqs.clear()
expectedFreqs.insert_rows(exp_freqs)
set_row_height(expectedFreqs, '1:13', 20)
set_column_width(expectedFreqs, 'A:N', 50)

zeros = [[0 for _ in range(13)] for _ in range(13)]
actualFreqs.update("A1:M13", zeros)
set_row_height(actualFreqs, '1:13', 20)
set_column_width(actualFreqs, 'A:N', 50)
actualFreqs.update_acell("A15", 0)

#currentSession.clear()
currentSession.format("A1:M13", {"backgroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0}})
#currentSession.insert_rows(hands)
set_row_height(currentSession, '1:13', 45)
set_column_width(currentSession, 'A:N', 50)

done = False
handsPlayed = 0

while (not done):
    action = input("Type in a hand, reset, random, or done: ")
    if (action == "reset"):
        handsPlayed = 0
        actualFreqs.update("A1:M13", zeros)
        actualFreqs.update_acell("A15", 0)
        currentSession.format("A1:M13", {"backgroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0}})
        print("Hands reset.")
    elif (action == "done"):
        done = True
        print("Session completed. See results in corresponding sheet.")
    elif (action == "random"):
        csv_file_path = 'hands.csv'
        with open(csv_file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            for hand in csv_reader:
                #print(hand[0])
                time.sleep(2)
                handFound = False
                for cell in currentSession.range("A1:M13"):
                    if (hand[0] == cell.value):
                        handFound = True
                        actualFreqs.update_acell(cell.address, int(actualFreqs.acell(cell.address).value) + 1)
                        actualFreqs.update_acell("A15", handsPlayed + 1)
                        handsPlayed += 1
                        break
                if (not handFound):
                    print("Hand not found. Try again.")
        print("Random distribution inserted.")
    else:
        handFound = False
        for cell in currentSession.range("A1:M13"):
            if (action == cell.value):
                handFound = True
                actualFreqs.update_acell(cell.address, int(actualFreqs.acell(cell.address).value) + 1)
                actualFreqs.update_acell("A15", handsPlayed + 1)
                handsPlayed += 1
                break
        if (not handFound):
            print("Hand not found. Try again.")
            

    