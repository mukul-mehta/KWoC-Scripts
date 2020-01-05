import os
import requests
import csv
import time


def check_username(username):
    print("Checking for user: {}".format(username))
    url = "https://github.com/".format(username)
    r = requests.get(url)
    print("Status Code: {}\n\n".format(str(r.status_code)))
    flag = False
    
    if r.status_code == 200:
        flag = True
    
    time.sleep(5)
    return flag

correct_handles = open("correct_handles.csv", "a+")
incorrect_handles = open("incorrect_handles.csv", "a+")

correct_writer = csv.writer(correct_handles)
incorrect_writer = csv.writer(incorrect_handles)

with open("data.csv") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        username = row[1]
        if username is None:
            incorrect_writer.writerow(row)
            continue

        else:
            if check_username(username):
                correct_writer.writerow(row)
            else:
                incorrect_writer.writerow(row)