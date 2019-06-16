import email
import imaplib
from bs4 import BeautifulSoup
import os
import mimetypes

username = '631581305@qq.com'
password = 'stnigyzqgsvuvbeaf'

mail = imaplib.IMAP4_SSL("imap.qq.com")
mail.login(username, password)


mail.select("inbox")
#mail.create("Item2")

#mail.list()

result, data = mail.uid('search', None, "ALL")

inbox_item_list = data[0].split()

for item in inbox_item_list:
    
    #most_recent = inbox_item_list[-1]

    #oldest = inbox_item_list[0]

    result2, email_data = mail.uid('fetch', item,'(RFC822)')

    raw_email = email_data[0][1].decode("utf-8")

    email_message = email.message_from_string(raw_email)

    to_ = email_message['To']
    from_ = email_message['From']
    subject_ = email_message['Subject']
    date_ = email_message['date']
    counter = 1
    for part in email_message.walk():
        if part.get_content_maintype() == "multipart":
            continue
        filename = part.get_filename()
        content_type = part.get_content_type()
        if not filename:
            #ext = ".html"
            ext = mimetypes.guess_extension(content_type)
            if not ext:
                ext = '.bin'
            filename = "msg-part-%08d%s" %(counter, ext)
        counter += 1

    save_path = os.path.join(os.getcwd(), "emails", date_, subject_)
    
"""
    if  not os.path.exists(save_path):
        os.makedirs(save_path)
    with open(os.path.join(save_path, filename), 'wb') as fp:
        fp.write(part.get_payload(decode=True))



    
        content_type = part.get_content_type()
        #print(subject_)
        #print(content_type)
        if "plain" in content_type:
            #print(part.get_payload())
            pass
        elif "html" in content_type:
            html_ = part.get_payload()
            soup = BeautifulSoup(html_, "html.parser")
            text = soup.get_text()
            print(subject_)
            print(text)
        else:
            pass
            #print(content_type)
        
"""       
            

        


    #email_message.get_payload()
