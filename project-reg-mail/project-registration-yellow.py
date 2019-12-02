import os
import csv
from mail import send_mail

def create_message(name, project):
    message = """
    Hello {}, <br><br>
    Greetings from KOSS! <br>

    Thank you for registering your project {} for KWoC 19.<br>
    It has come to our notice that your GitHub repository link or the communication channel link is invalid. We request you to re-register this project with proper links and make sure that the links used have not expired.<br>
    You may go through the mentor manual once and always feel free to mail us whenever required.<br><br>
    It is a critical issue so please try to fix it as soon as possible. Failing to do so will force us to remove your project from KWoC 19.
    The registration link is given below.
    https://docs.google.com/forms/d/e/1FAIpQLSfXyuX0EZ_X9GmBPQMuo-GprZGQgwaDl1r93-yl9RE_Saws1w/viewform 
    <br><br>
    Regards, <br>
    Kharagpur Open Source Society.
    """.format(name, project)

    return message

with open('yellow-projects-list.csv', mode='r') as csv_file:
    successful_mails = []
    unsuccessful_mails = []
    subject = "Action required for your project in KWoC '19!"
    csv_reader = csv.DictReader(csv_file, fieldnames=['Name', 'Email', 'Project'])
    for row in csv_reader:
        body = create_message(row["Name"], row["Project"])
        try:
            send_mail(row["Email"], subject, body)
            successful_mails.append(row["Email"])
        except Exception as e:
            print(e)
            unsuccessful_mails.append(row["Email"])
    
    print(len(successful_mails))    
