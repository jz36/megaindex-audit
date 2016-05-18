from tkinter import *
import requests
import urllib.parse
import time
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders as Encoders
import os
import pdb

def indexSite(site, customerEmail, customerFIO):
	methods = ('reindex_site', 'get_index')

	BASE_URL = 'http://api.megaindex.ru/?'

	paramsForReIndex = {
		'method': methods[0],
		'output': 'json',
		'mode': 'site',
		'login': 'dmitriy@biksileev.ru',
		'password': 'NokiaN9777',
		'url': site,
		'target': 'reindex',
		'version_id': '1',
		'count_page': '30'
	}

	#pdb.set_trace()

	firstResponse = requests.get(BASE_URL, params=paramsForReIndex)
	firstJson = firstResponse.json()

	paramsForGetIndex = {
		'method': methods[1],
		'login': 'dmitriy@biksileev.ru',
		'password': 'NokiaN9777',
		'url': site,
		'version_id': firstJson['version_id']
	}

	time.sleep(300)

	secondResponse = requests.get(BASE_URL, params=paramsForGetIndex)
	secondJson = secondResponse.json()

	f = open('textJson.txt', 'w')
	f.write(str(secondJson))
	f.close()

	subject = 'Аудит сайта ' + site

	message = "Добрый день, " + customerFIO + ". Провели аудит вашего сайта."

	sendMail(customerEmail, subject, message)

def sendMail(emailTo, subject, msgText):
	filepath = "/home/jz36/Документы/chess/bBishop.png"
	basename = os.path.basename(filepath)
	address = "neo@biksileev.ru"

	# Compose attachment
	part = MIMEBase('application', "octet-stream")
	part.set_payload(open(filepath,"rb").read() )
	Encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename)
	part2 = MIMEText(msgText, 'plain')

	# Compose message
	msg = MIMEMultipart()
	msg['From'] = address
	msg['To'] = emailTo
	msg['Subject'] = subject

	msg.attach(part2)
	msg.attach(part)

	# Send mail
	smtp = SMTP_SSL()
	smtp.connect('smtp.yandex.ru')
	smtp.login(address, 'rjcjq12utybq')
	smtp.sendmail(address, emailTo, msg.as_string())
	smtp.quit()

def proof(event):
	#pdb.set_trace()
	print('Start work!')
	indexSite(siteEntry.get(), emailEntry.get(), nameEntry.get())
	print('Done!')
	siteEntry.delete(0, len(siteEntry.get()))
	emailEntry.delete(0, len(emailEntry.get()))
	nameEntry.delete(0, len(nameEntry.get()))

root = Tk()

mainFrame = Frame(root,width=500,height=100,bd=5)

nameLabel = Label(mainFrame, text='ФИО клиента:')

nameEntry = Entry(mainFrame)

siteLabel = Label(mainFrame, text='Сайт клиента:')

siteEntry = Entry(mainFrame)

emailLabel = Label(mainFrame, text='E-mail клиента:')

emailEntry = Entry(mainFrame)

buttonSend = Button(mainFrame, text='Send')

'''mainFrame.grid(row=0,column=0,rowspan=6,columnspan=2)

nameLabel.grid(row=0,column=0)

nameEntry.grid(row=1,column=0, columnspan=2)

siteLabel.grid(row=2,column=0)

siteEntry.grid(row=3,column=0, columnspan=2)

emailLabel.grid(row=4,column=0)

emailEntry.grid(row=5,column=0, columnspan=2)'''

buttonSend.bind("<Button-1>", proof)

mainFrame.pack()

nameLabel.pack()

nameEntry.pack()

siteLabel.pack()

siteEntry.pack()

emailLabel.pack()

emailEntry.pack()

buttonSend.pack()

root.mainloop()
