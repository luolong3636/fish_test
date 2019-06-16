import os
import smtplib
from email.message import EmailMessage
import imghdr

EMAIL_ADDRESS = '631581305@qq.com'
EMAIL_PASSWORD = 'stnigyzqgsvuvbeaf'

msg = EmailMessage()
msg['Subject'] = '使用emailmessage类发送邮件！！！'
msg['From'] = EMAIL_ADDRESS
msg['To'] = "631581305@qq.com"

msg.set_content('这是邮件的主要内容')

with open('p5.JPG', 'rb') as f:
    file_date = f.read()
    file_type = imghdr.what(f.name)
    #print(file_type)
    file_name = f.name
    #print(file_name)

msg.add_attachment(file_date, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL("smtp.qq.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)



'''

with smtplib.SMTP("smtp.qq.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)


    subject= "这是标题《发送测试第一版》"
    body = "《这是邮件内容》"
    msg = f'Subject: {subject}\n\n{body}'
    msg = msg.encode()
    #print(msg)
    smtp.sendmail(EMAIL_ADDRESS, 'lxyzjmll@gmail.com', msg)
    
'''
