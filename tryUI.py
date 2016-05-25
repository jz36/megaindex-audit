from tkinter import *
from tkinter.filedialog import *
import fileinput
#import requests
import urllib.parse
import time
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.headerregistry import Address
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders as Encoders
import os
from pdb import set_trace
from wkhtmltopdfwrapper import WKHtmlToPdf


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
	address = "biksileev.email@yandex.ru"

	# Compose attachment
	part = MIMEBase('application', "octet-stream")
	part.set_payload(open(filepath,"rb").read() )
	Encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename)
	part3 = MIMEBase('application', "octet-stream")
	part3.set_payload(open(os.getcwd() + '/plan_rabot_po_saitu_na_god.xlsx',"rb").read() )
	Encoders.encode_base64(part3)
	part3.add_header('Content-Disposition', 'attachment; filename="plan_rabot_po_saitu_na_god.xlsx"')
	part2 = MIMEText(msgText, 'plain')

	# Compose message
	msg = MIMEMultipart()
	msg['From'] = 'Михаил Юрьевич Бубновский <sales@biksileev.ru>'
	msg['To'] = emailTo
	msg['Subject'] = subject

	msg.attach(part2)
	msg.attach(part)
	msg.attach(part3)

	# Send mail
	smtp = SMTP_SSL()
	smtp.connect('smtp.yandex.ru')
	smtp.login(address, 'biksileev')
	smtp.sendmail(address, emailTo, msg.as_string())
	smtp.quit()

def proof(event):
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
	
	file = WKHtmlToPdf()

	def clearStr( string ):
		if type(string) != type(None):
			return string.replace('\n','').replace('\t','').replace('\r','')

	g = Grab()

	g.go('https://id.pr-cy.ru/signup/login/')

	g.doc.set_input('login_email','neo@biksileev.ru') 
	g.doc.set_input('password','biksileev')
	g.doc.submit()
	output = open('Finished.txt', 'w')

	j = 1

	for string in fileinput.input(fileAddr):

		customerList = string.split('	')

		customerList[2] = clearStr(customerList[2])

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
				<!--<img src="biksileev.jpg"/>-->
				<h1>Технический аудит сайта http://''' + customerList[1] + '''</h1>
				<p>Для чёткого понимания текущего технического состояния сайта http://''' + customerList[1] + '''
был проведён полный технический аудит, результаты которого представлены ниже в виде таблицы.</p></div>''')
		f.write('<div>')
		f.write('<table>')
		f.write('<thead><tr><td colspan="2">Технический аудит</td></tr></thead>')
		f.write('<tbody>')
		f.write('<tr><td>Критерий</td><td>Текущее состояние</td></tr>')

		for name in newList:
			if True: #not('Обратные ссылки' in name.cssselect('.info-test')[0].text) or not('Аналитика' in name.cssselect('.info-test')[0].text):
				if len(name.cssselect('.info-test')) > 0:
					if (('Описание страницы' or 'Скриншот сайта на смартфоне') in name.cssselect('.info-test')[0].text):
						f.write('</table></div><div class="pageBreak"><table>')
						f.write('<tr ><td class="left">')
					else:
						f.write('<tr><td class="left">')
					f.write(name.cssselect('.info-test')[0].text)
					f.write('</td>')
					f.write(' ')
					if len(name.cssselect('.content-test')) > 0:
						if (len(clearStr(name.cssselect('.content-test')[0].text)) > 0):
							if (name.cssselect('.check-test')[0].get('test-status') == 'success'):
								f.write('<td class="right success">')
							elif (name.cssselect('.check-test')[0].get('test-status') == 'fail'):
								f.write('<td class="right unsuccess">')
							else:
								f.write('<td class="right">')
							if (len(name.cssselect('.content-test')[0].cssselect('a')) > 0): 
								f.write(clearStr(name.cssselect('.content-test')[0].text) + clearStr(name.cssselect('.content-test')[0].cssselect('a')[0].text))
							else:
								f.write(clearStr(name.cssselect('.content-test')[0].text))
							f.write('</td>')
						elif (len(name.cssselect('.content-test')[0].cssselect('.iphone .iphone-screen img')) > 0):
							if (name.cssselect('.check-test')[0].get('test-status') == 'success'):
								f.write('<td class="right success">')
							elif (name.cssselect('.check-test')[0].get('test-status') == 'fail'):
								f.write('<td class="right unsuccess">')
							else:
								f.write('<td class="right">')
							f.write('<img src="http://' + name.cssselect('.content-test')[0].cssselect('.iphone .iphone-screen img')[0].get('src')[2:] + '">')
							f.write('</td>')
						elif(('Facebook' in name.cssselect('.info-test')[0].text) or ('ВКонтакте' in name.cssselect('.info-test')[0].text) or ('Google+' in name.cssselect('.info-test')[0].text) or ('Twitter' in name.cssselect('.info-test')[0].text)):
							if(name.cssselect('.check-test')[0].get('test-status') == 'success'):
								f.write('<td class="right success">')
								f.write('Ссылка на страницу найдена.')
								f.write('</td>')
							elif(name.cssselect('.check-test')[0].get('test-status') == 'fail'):
								f.write('<td class="right unsuccess">')
								f.write('Ссылка на страницу не найдена.')
								f.write('</td>')
						elif ((len(name.cssselect('.content-test')[0].cssselect('a')) > 0)):
							if (name.cssselect('.check-test')[0].get('test-status') == 'success'):
								f.write('<td class="right success">')
							elif (name.cssselect('.check-test')[0].get('test-status') == 'fail'):
								f.write('<td class="right unsuccess">')
							else:
								f.write('<td class="right">')
							f.write(clearStr(name.cssselect('.content-test')[0].cssselect('a')[0].text))
							f.write('</td>')
						elif (len(name.cssselect('.content-test')[0].cssselect('p')) > 0):
							newList2 = name.cssselect('.content-test')[0].cssselect('p')
							if (name.cssselect('.check-test')[0].get('test-status') == 'success'):
								f.write('<td class="right success">')
							elif (name.cssselect('.check-test')[0].get('test-status') == 'fail'):
								f.write('<td class="right unsuccess">')
							else:
								f.write('<td class="right">')
							for paragraph in newList2:
								f.write(clearStr(paragraph.text))
								f.write('<br>')
							f.write('</td>')
						elif (len(name.cssselect('.content-test')[0].cssselect('.progress-info .progress-info')) > 0):
							if (name.cssselect('.check-test')[0].get('test-status') == 'success'):
								f.write('<td class="right success">')
							elif (name.cssselect('.check-test')[0].get('test-status') == 'fail'):
								f.write('<td class="right unsuccess">')
							else:
								f.write('<td class="right">')
							f.write(clearStr(name.cssselect('.content-test')[0].cssselect('.progress-info .progress-info')[0].text))
							f.write('</td>')
						elif (len(name.cssselect('.content-test')[0].cssselect('.progress-info')) > 0):
							if (name.cssselect('.check-test')[0].get('test-status') == 'success'):
								f.write('<td class="right success">')
							elif (name.cssselect('.check-test')[0].get('test-status') == 'fail'):
								f.write('<td class="right unsuccess">')
							else:
								f.write('<td class="right">')
							f.write(clearStr(name.cssselect('.content-test')[0].cssselect('.progress-info')[0].text))
							f.write('</td>')
						elif (len(name.cssselect('.content-test')[0].cssselect('span')) > 0) or ('Системы статистики' in name.cssselect('.info-test')[0].text):
							if (name.cssselect('.check-test')[0].get('test-status') == 'success'):
								f.write('<td class="right success">')
							elif (name.cssselect('.check-test')[0].get('test-status') == 'fail'):
								f.write('<td class="right unsuccess">')
							else:
								f.write('<td class="right">')
							newList2 = name.cssselect('.content-test')[0].cssselect('span')
							for analytics in newList2:
								f.write(clearStr(analytics.text))
								f.write('<br>')
							f.write('</td>')
					elif (len(name.cssselect('.info-test')) > 0):
						if('Местоположение сервера' in name.cssselect('.info-test')[0].text):
							if (name.cssselect('.check-test')[0].get('test-status') == 'success'):
								f.write('<td class="right success">')
							elif (name.cssselect('.check-test')[0].get('test-status') == 'fail'):
								f.write('<td class="right unsuccess">')
							else:
								f.write('<td class="right">')
							f.write(name.cssselect('.content-test img')[0].get('alt').split(' ')[2])
							f.write('</td>')
						elif('Favicon' in name.cssselect('.info-test')[0].text):
							if(name.cssselect('.check-test')[0].get('test-status') == 'success'):
								f.write('<td class="right success">')
								f.write('Отлично, у сайта есть Favicon.')
								f.write('</td>')
							elif(name.cssselect('.check-test')[0].get('test-status') == 'fail'):
								f.write('<td class="right success">')
								f.write('Отлично, у сайта есть Favicon.')
								f.write('</td>')
			i += 1
			'''f.write('<td>')
			newList3 = name.cssselect('.description p')
			for paragraph in newList3:
			f.write(paragraph.text)'''
		f.write('</tbody>')
		f.write('</table>')
		f.write('''<p> Резолюция
Сайт частично оптимизирован.</p>
		</body>
		</html>
			''')
		f.close()
		file.render('file://' + os.getcwd() + '/audit/' + customerList[1] + '.html', 'audit/' + customerList[1] + '.pdf')
		subject = customerList[0] + ' - подготовили аудит вашего сайта: ' + customerList[1]
		message = customerList[0] + """, добрый день!

Причина нашего обращения к Вам не случайна.

Специалистами студии Дмитрия Биксилеева в течение марта месяца проводился выборочный аудит сайтов компаний работающих в сфере услуг для бизнеса. В том числе был проведен краткий аудит Вашего сайта %s

Нашими SEO-специалистами выявлены достаточно серьезные ошибки на сайте, мешающие его продвижению в поисковых системах и снижающие удобство пользования вашим сайтом для ваших потенциальных клиентов (см. приложение «Экспресс аудит сайта»). Как правило, данные ошибки не заметны на первый взгляд, но об их наличии убедительно свидетельствует низкий КПД сайта.

Наверное, и Вы сами, как ответственный и экономный хозяин, периодически задаетесь вопросом:

Почему сайт, в который вложено столько интеллектуальных и финансовых ресурсов не оправдывает свое существование?
Почему клиенты заходят на сайт, но не совершают покупок?
Почему Ваши конкуренты уводят клиентов?

Мы дадим ответы на все интересующие Вас вопросы и с удовольствием поделимся самыми свежими и самыми необходимыми в XXI веке знаниями по интернет-маркетингу. В случае Вашей заинтересованности, сделаем полный базовый, технический и юзабилити аудит сайта, предложим реальные сроки и способы устранения недостатков и выведем Ваш сайт на лидирующие позиции в поисковиках по самым высоко конверсионным запросам.

Мы не предлагаем Вам услуги с непредсказуемым или неубедительным результатом. Мы предлагаем взрывной рост Вашему Интернет-бизнесу!

Помогая Вам в бизнесе, мы становимся своеобразным хуком в интернет-продажах, Вашим директором по маркетингу, полностью выстраивающим маркетинг и систему продаж.

С уважением к Вам и Вашему бизнесу, Бубновский Михаил
Директор по развитию компании Студия Дмитрия Биксилеева

----------------------------------------------------------
Тел.: +7(343)298-03-54
Сот. Тел.: +7 (922)1554515
E-mail: sales@biksileev.ru
skype: ottepel_1
www.biksileev.ru""" % customerList[1]
		sendMail(customerList[2], subject, message, 'audit/' + customerList[1] + '.pdf')
		customerList.append('Отправлено')
		output.write('	'.join(customerList))
		output.write('\n')
		text1.delete('1.0', str(len('	'.join(customerList) + '\n') + 1) + '.0') 
		text1.insert(str(j) + '.0', '	'.join(customerList) + '\n')
		text1.update()
	output.close()



def openFile( event ):
	askopenfilename()

root = Tk()

text1=Text(root,height=3,width=70,font='Arial 12',wrap=WORD)

mainFrame = Frame(root,width=500,height=100,bd=5)

op = askopenfilename()

buttonStart = Button(mainFrame, text='Start')

'''nameLabel = Label(mainFrame, text="Ваше ФИО (полностью)")

nameEntry = Entry(mainFrame)

nameLabel = Label(mainFrame, text="Ваше ФИО (полностью)")

nameEntry = Entry(mainFrame)

nameLabel = Label(mainFrame, text="Ваше ФИО (полностью)")

nameEntry = Entry(mainFrame)
'''
buttonStart.bind("<Button-1>", proof2)

#op.bind("<Button-1>", openFile)

mainFrame.pack()

text1.pack()

#op.pack()

buttonStart.pack()

root.mainloop()
