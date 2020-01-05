import os
import csv
from mail import send_mail

def create_message(name):
    message = """
    Hola {}!<br><br>
    Greetings from KOSS! Hope you are having a great winter.<br>
    We hope you're actively contributing to projects and will continue to do so. <br><br>

    Some announcements:<br>
    1. As some students are facing issues contributing to projects due to the internet shutdown being imposed in various parts of India, we have decided to scrap the mid evals. This decision was taken after receiving numerous requests from concerned students.<br>
    2. The participating students will be judged directly on the basis of their contributions until the end-evals, that will take place on January 5.<br>
    3. The students must have at least one PR merged in their respective projects to be qualified to get a certificate.<br><br>
    We apologize for the inconvenience caused.<br><br>
    Wishing you all the best<br>
    Kharagpur Open Source Society
    """.format(name)

    return message

with open('incorrect_handles.csv', mode='r') as csv_file:
    successful_mails = []
    unsuccessful_mails = []
    subject = "Information regarding Mid-Evals for KWoC '19"
    csv_reader = csv.DictReader(csv_file, fieldnames=['name', 'handle', 'mail', 'insti'])
    for row in csv_reader:
        body = create_message(row['name'])
        try:
            send_mail(row["mail"], subject, body)
            successful_mails.append(row["mail"])
        except Exception as e:
            print(e)
            unsuccessful_mails.append(row["mail"])
    
    print(len(successful_mails))