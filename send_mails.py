
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
    <body style="margin: 0;">
    <div dir="rtl" style="background-color: rgb(191 219 254); color: black; padding: 30px 30px 800px 30px;">
        <div style="box-shadow: 1px 1px px black; border-radius: 20px;">
            <div style=" padding: 18px; background-color: rgb(30 64 175); color: black; border-radius: 20px 20px 0px 0px;">
                <div style="font-family: sans-serif; font-size: 24px; font-weight: bold; color: white; text-decoration: none;">דיבורים טובים</div>
            </div>
            <div style=" background-color: white; padding: 30px 30px 40px 30px; border-radius: 0px 0px 20px 20px;">
                <div style="font-size: 20px; padding: 0px 0px 10px 0px; font-family: sans-serif;">{subject}</div>
                <a style=" color: black; text-decoration: none;font-family: sans-serif;" href="tel:{message}">מספר טלפון:{message} </a>
            </div>
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






