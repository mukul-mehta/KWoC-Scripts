import os
import csv
from mail import send_mail

def create_message(name, project):
    message = """
    Hello {} <br><br>
    Greetings from KOSS!<br>
    This mail is to inform you regarding issues faced in acceptance of your project {} for KWoC this winter. <br>
    If your project doesn't have issues or has very few issues please add more issues and prepare a good README.md so that potential mentees have a better understanding of the project and it's easier for them to start working on it. <br>
    Have a look at this article to understand why this is important: http://www.bauva.com/blog/Writing-Kickass-READMEs/ <br>
    Please check your communication channel link and if it is not working, please provide a valid communication channel link. <br>
    Please address the above issues and give a confirmation reply by 6th December 2019. <br><br>
    Regards, <br>
    Kharagpur Open Source Society
    """.format(name, project)

    return message

with open('blue-projects-list.csv', mode='r') as csv_file:
    successful_mails = []
    unsuccessful_mails = []
    subject = "Issues in your project submission for KWoC '19"
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