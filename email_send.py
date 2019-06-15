import os
import smtplib

EMAIL_ADDRESS = '631581305@qq.com'
EMAIL_PASSWORD = 'tnigyzqgsvuvbeaf'

with smtplib.SMTP("smtp.qq.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)


    subject= "这是标题《发送测试第一版》"
    body = "《这是邮件内容》"
    msg = f'Subject: {subject}\n\n{body}'
    msg = msg.encode()
    smtp.sendmail(EMAIL_ADDRESS, '631581305@qq.com', msg)
