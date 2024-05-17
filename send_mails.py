
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(mail_data):
    
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.ehlo()
    smtp_object.starttls()
    
    password = os.environ['PASSWORD']
    email = os.environ['EMAIL']
    smtp_object.login(email, password)

    from_address = email
    to_address = mail_data['email']
    subject = mail_data['subject']
    message = mail_data['message']

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address
    # msg = f'Subject: {subject}\n{message}'
    text = message
    html = f"""\
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <div dir="rtl" style="background-color: #EEF2FF; color: black; ">
            <div style=" padding: 10px; background-color: #A5B4FB; color: black; ">
                <div style="font-size: large; font-weight: bold; color: black; text-decoration: none;">דיבורים טובים</div>
            </div>
            <div style="padding: 20px;">
                <p>{subject}</p>
                <a style="font-weight: bold; color: black; text-decoration: none;" href="tel:{message}">{message}</a>
            </div>
        </div>
    </body>
    </html>
    """
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)

    smtp_object.sendmail(from_address, to_address, msg.as_string())
    smtp_object.quit()
    

    return mail_data  






