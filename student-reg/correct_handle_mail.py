import os
import csv
from mail import send_mail

def create_message(name):
    message = """
    Hello {} <br><br>
    Greetings from KOSS! We're glad to inform you that you have successfully registered for KWoC '19. <br><br>
    We apologise for the incorrect mail sent previously. <br><br>
    You should look up projects on: https://kwoc.kossiitkgp.org/projects/ and join the communication channels of those which interest you. Don't hesitate to talk to mentors and ask them your questions. <br><br>
    The coding period officially begins on 7th December 2019. Once the coding period begins, your contributions will be considered for statistics! <br><br>
    Do check out the students manual: https://kwoc.kossiitkgp.org/static/files/KWoCStudentManual.pdf <br>
    Join the official KWoC Slack workspace: https://join.slack.com/t/kwoc-koss/shared_invite/enQtODc2NTgwNTc0ODA3LWU5MzVkMWUzMzZmNzI4OWM3M2NiMjA3NmNkODk2MTQwMTE4YmJiYmUzZjZkMDZjYzQ4YzE0MTliMmViMDQ3YzY <br><br>
    Thank You, <br> 
    Kharagpur Open Source Society
    """.format(name)

    return message

successful_mails = []
unsuccessful_mails = []

with open('correct_handles.csv', mode='r') as csv_file:
    subject = "You've successfully registered for KWoC '19!"
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        body = create_message(row[0])
        try:
            send_mail(row[2], subject, body)
            successful_mails.append(row[2])
        except Exception as e:
            print(e)
            unsuccessful_mails.append(row[2])
    
    print("Successful Mails: " + str(len(successful_mails)))
    print("Unsuccessful Mails: " + str(len(unsuccessful_mails)))
print(unsuccessful_mails)