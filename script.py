import os,imaplib,email,subprocess,time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import decode_header
from ansi2html import Ansi2HTMLConverter
from flask import Flask

app = Flask(__name__)


mail = ''
pas = ''
number = ''
imap_server = ''

def get_text(mail,pas,number,imap_host):
	imap = imaplib.IMAP4_SSL(imap_host)
	imap.login(mail, pas)
	imap.select('Inbox')
	result,data = imap.uid('search',None,"ALL")
	inbox_item = data[0].split()
	most_recent = inbox_item[-1]
	result2,email_data = imap.uid('fetch',most_recent,'(RFC822)')
	raw_email = email_data[0][1].decode("utf-8")
	b = email.message_from_string(raw_email,policy = email.policy.default)
	mail_bytes = []
	if b['From'] == number and b.is_multipart() == True:
	    print('You Recieved a message from:'  + b['From'])
	    for p in b.get_payload():
	        mail_bytes.append(p.get_payload(decode=True))
	    return mail_bytes[1].decode('utf-8')
	elif b['From'] == number:
	    return b.get_payload(decode=True).decode('utf-8').strip()
	else:
		return "No command from email yet try refreshing the page"



def command_to_html(cmd):
	print(str(cmd))
	command = os.popen(cmd)
	conv = Ansi2HTMLConverter()
	ansi = "".join(command.read())
	html = conv.convert(ansi)
	return html



@app.route('/')
def index():
	time.sleep(10)
	command = get_text(mail,pas,number,imap_server)
	return f"You ran {command}\n\n {command_to_html(command)}"





if __name__ == '__main__':
	app.run()

