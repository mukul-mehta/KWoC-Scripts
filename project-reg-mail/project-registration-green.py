import os
import csv
from mail import send_mail

def create_message(name, project):
    message = """
    Hello {}, <br><br>
    
    Greetings from KOSS! <br>
    Your project {} is successfully selected for KWoC. Thank you for submitting your project for students to contribute and learn.
    Students who are interested in your project will contact you via your chat invitation link. Please help them learn and develop their skills during this period. <br><br>
    Regards, <br>
    Kharagpur Open Source Society.
    """.format(name, project)

    return message

with open('green-projects-list.csv', mode='r') as csv_file:
    successful_mails = []
    unsuccessful_mails = []
    subject = "Project selection confirmation for KWoC '19!"
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
