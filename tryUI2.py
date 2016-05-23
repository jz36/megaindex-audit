# -*- coding: utf-8 -*- 
from Tkinter import *
from tkFileDialog import *
import fileinput
import urllib2.requests
import urllib.parse
import time
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders as Encoders
import os
from pdb import set_trace

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

def sendMail(emailTo, subject, msgText, fileAddr):
	filepath = fileAddr
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

def proof2(event):
	grabPRCY(op)

def grabPRCY(fileAddr):
	from grab import Grab

	def clearStr( string ):
		return string.replace('\n','').replace('\t','').replace('\r','')

	g = Grab()

	g.go('https://id.pr-cy.ru/signup/login/')

	g.doc.set_input('login_email','neo@biksileev.ru') 
	g.doc.set_input('password','biksileev')
	g.doc.submit()

	for string in fileinput.input(fileAddr):

		customerList = string.split('	')

		g.go('https://a.pr-cy.ru/' + customerList[1])

		time.sleep(10)

		newList = g.css_list('.is')

		i = 0

		f = open('audit/' + customerList[1] + '.html','w')
		f.write('''<!DOCTYPE html>
	<html>
		<head>
			<meta charset="utf-8" />
			<link rel='stylesheet' href="style.css">
		</head>
		<body>
			<div id="head">
				<img src="biksileev.jpg"/>
				<h1>Технический аудит сайта http://''' + customerList[1] + '''</h1>
				<p>Для чёткого понимания текущего технического состояния сайта http://''' + customerList[1] + '''
был проведён полный технический аудит, результаты которого представлены ниже в виде таблицы.</p></div>''')
		f.write('<table>')
		f.write('<thead><tr><td colspan="2">Технический аудит</td></tr></thead>')
		f.write('<tbody>')
		f.write('<tr><td>Критерий</td><td>Текущее состояние</td></tr>')

		for name in newList:
			if True: #not('Обратные ссылки' in name.cssselect('.info-test')[0].text) or not('Аналитика' in name.cssselect('.info-test')[0].text):
				f.write('<tr><td class="left">')
				if len(name.cssselect('.info-test')) > 0:
					f.write(name.cssselect('.info-test')[0].text)
					f.write('</td>')
					f.write(' ')
					if len(name.cssselect('.content-test')) > 0:
						if (len(clearStr(name.cssselect('.content-test')[0].text)) > 0):
							f.write('<td class="right">')
							f.write(clearStr(name.cssselect('.content-test')[0].text))
							f.write('</td>')
						elif (len(name.cssselect('.content-test')[0].cssselect('.iphone .iphone-screen img')) > 0):
							f.write('<td class="right">')
							f.write('<img src="http://' + name.cssselect('.content-test')[0].cssselect('.iphone .iphone-screen img')[0].get('src')[2:] + '">')
							f.write('</td>')
						elif (len(name.cssselect('.content-test')[0].cssselect('a')) > 0):
							f.write('<td class="right">')
							f.write(clearStr(name.cssselect('.content-test')[0].cssselect('a')[0].text))
							f.write('</td>')
						elif (len(name.cssselect('.content-test')[0].cssselect('p')) > 0):
							newList2 = name.cssselect('.content-test')[0].cssselect('p')
							f.write('<td class="right">')
							for paragraph in newList2:
								f.write(clearStr(paragraph.text))
								f.write('<br>')
							f.write('</td>')
						elif (len(name.cssselect('.content-test')[0].cssselect('.progress-info .progress-info')) > 0):
							f.write('<td class="right">')
							f.write(clearStr(name.cssselect('.content-test')[0].cssselect('.progress-info .progress-info')[0].text))
							f.write('</td>')
						elif (len(name.cssselect('.content-test')[0].cssselect('.progress-info')) > 0):
							f.write('<td class="right">')
							f.write(clearStr(name.cssselect('.content-test')[0].cssselect('.progress-info')[0].text))
							f.write('</td>')
						elif (len(name.cssselect('.content-test')[0].cssselect('span')) > 0) or ('Системы статистики' in name.cssselect('.info-test')[0].text):
							f.write('<td class="right">')
							newList2 = name.cssselect('.content-test')[0].cssselect('span')
							for analytics in newList2:
								f.write(clearStr(analytics.text))
								f.write('<br>')
							f.write('</td>')
					elif (len(name.cssselect('.info-test')) > 0):
						if('Местоположение сервера' in name.cssselect('.info-test')[0].text):
							f.write('<td class="right">')
							f.write(name.cssselect('.content-test img')[0].get('alt').split(' ')[2])
							f.write('</td>')
						elif(('Facebook' in name.cssselect('.info-test')[0].text) or ('ВКонтакте' in name.cssselect('.info-test')[0].text) or ('Google+' in name.cssselect('.info-test')[0].text) or ('Twitter' in name.cssselect('.info-test')[0].text)):
							if(name.getparent().cssselect('.check-test')[0].get('test-status') == 'success'):
								f.write('<td class="right">')
								f.write('Ссылка на страницу найдена.')
								f.write('</td>')
						elif('Favicon' in name.cssselect('.info-test')[0].text):
							if(name.getparent().cssselect('.check-test')[0].get('test-status') == 'success'):
								f.write('<td class="right">')
								f.write('Отлично, у сайта есть Favicon.')
								f.write('</td>')
			i += 1
			'''f.write('<td>')
			newList3 = name.cssselect('.description p')
			for paragraph in newList3:
			f.write(paragraph.text)'''
			f.write('</tr>')
				#f.write('</td></tr>')
				#f.write('\n')
		print(i)
		f.write('</tbody>')
		f.write('</table>')
		f.write('''
		</body>
		</html>
			''')
		f.close()
		subject = 'Аудит сайта ' + customerList[1]
		message = "Добрый день, " + customerList[0] + ". Провели аудит вашего сайта."
		#sendMail(customerList[2], subject, message, 'audit/' + customerList[1] + '.html')
		#sendMail('texpomruu@yandex.ru', subject, message, 'audit/' + customerList[1] + '.html')
		#time.sleep(10)
		print(customerList[0])

root = Tk()

mainFrame = Frame(root,width=500,height=100,bd=5)

op = askopenfilename()

buttonStart = Button(mainFrame, text='Start')

buttonStart.bind("<Button-1>", proof2)

mainFrame.pack()

buttonStart.pack()

root.mainloop()
