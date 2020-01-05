import os
import csv
from mail import send_mail

def create_message():
    message = """
    Hola Mentors!<br><br>
    Greetings from KOSS! Hope you are having a great winter.<br>
    Some announcements:<br>
    1. As some students are facing issues contributing to projects due to the internet shutdown being imposed in various parts of India, we have decided to scrap the mid evals. This decision was taken after receiving numerous requests from concerned students.<br>
    2. The participating students will be judged directly on the basis of their contributions until the end-evals, that will take place on January 5.<br>
    3. The students must have at least one PR merged in their respective projects to be qualified to get a certificate.<br><br>
    We apologize for the inconvenience caused.<br><br>
    Wishing you all the best<br>
    Kharagpur Open Source Society
    """

    return message

with open('yellow-projects-list.csv', mode='r') as csv_file:
    successful_mails = []
    unsuccessful_mails = []
    subject = "Information regarding Mid-Evals for KWoC '19"
    csv_reader = csv.DictReader(csv_file, fieldnames=['Name', 'Email', 'Project'])
    for row in csv_reader:
        body = create_message()
        try:
            send_mail(row["Email"], subject, body)
            successful_mails.append(row["Email"])
        except Exception as e:
            print(e)
            unsuccessful_mails.append(row["Email"])
    
    print(len(successful_mails))