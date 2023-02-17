import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Set email addresses and credentials
sender_email = 'sonutinu568@gmail.com'
sender_password = '10March@2016'
recipient_email = 'tukarulganesh@gmail.com'

# Create message container
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = 'Subject of the email'

# Attach Excel file to the email
with open('D:\Python\ETL Operations with Python\Files\LookupMatchExampleOp.xlsx', 'rb') as file:
    attachment = MIMEApplication(file.read(), _subtype='xlsx')
    attachment.add_header('Content-Disposition', 'attachment', filename='example.xlsx')
    msg.attach(attachment)

# Create SMTP session for sending the mail
server = smtplib.SMTP('smtp.gmail.com', 587)
#server = smtplib.SMTP('imap.gmail.com', 993 )
server.starttls()
server.login(sender_email, sender_password)

# Send the message via the SMTP server
server.sendmail(sender_email, recipient_email, msg.as_string())
server.quit()
