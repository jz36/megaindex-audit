from grab import Grab
from ipdb import set_trace

def clearStr( string ):
	return string.replace('\n','').replace('\t','').replace('\r','')

g = Grab()

g.go('https://id.pr-cy.ru/signup/login/')

g.doc.set_input('login_email','neo@biksileev.ru') 
g.doc.set_input('password','biksileev')
g.doc.submit()
g.go('https://a.pr-cy.ru/personabook.ru')

newList = g.css_list('.is')

i = 0

f = open('prcy.html','w')
f.write('''
<html>
<head>
	<meta charset="utf-8" />
</head>
<body>
	''')
f.write('<table>')

for name in newList:
	try:
		'''if 'Скриншот сайта на смартфоне' in name.cssselect('.info-test')[0].text:
									set_trace()'''
		if not('Обратные ссылки' in name.cssselect('.info-test')[0].text) or not('Аналитика' in name.cssselect('.info-test')[0].text):
			tempVar = name.cssselect('.info-test')[0].text
			set_trace()
			f.write('<tr><td>')
			f.write(name.cssselect('.info-test')[0].text)
			f.write('</td>')
			f.write(' ')
			try:
				newVar = name.cssselect('.content-test')[0].text
				newVar = newVar.replace('\n','')
				newVar = newVar.replace('\t','')
				newVar = newVar.replace('\r','')
				if len(newVar) > 0:
					f.write('<td>')
					f.write(newVar)
					f.write('</td>')
				elif('Местоположение сервера' in name.cssselect('.info-test')[0].text):
					f.write('<td>')
					f.write(name.cssselect('.content-test img')[0].get('alt').split(' ')[2])
					f.write('</td>')
				elif(('Facebook' in name.cssselect('.info-test')[0].text) or ('ВКонтакте' in name.cssselect('.info-test')[0].text) or ('Google+' in name.cssselect('.info-test')[0].text) or ('Twitter' in name.cssselect('.info-test')[0].text)):
					if(name.getparent().cssselect('.check-test')[0].get('test-status') == 'success'):
						f.write('<td>')
						f.write('Ссылка на страницу найдена.')
						f.write('</td>')
				elif('Favicon' in name.cssselect('.info-test')[0].text):
					if(name.getparent().cssselect('.check-test')[0].get('test-status') == 'success'):
						f.write('<td>')
						f.write('Отлично, у сайта есть Favicon.')
						f.write('</td>')
				elif (len(name.cssselect('.content-test')[0].cssselect('.iphone .iphone-screen img')) > 0):
					f.write('<td>')
					f.write('<img src="http://' + name.cssselect('.content-test')[0].cssselect('.iphone .iphone-screen img')[0].get('src')[2:] + '">')
					f.write('</td>')
				elif (len(name.cssselect('.content-test')[0].cssselect('a')) > 0):
					f.write('<td>')
					f.write(clearStr(name.cssselect('.content-test')[0].cssselect('a')[0].text))
					f.write('</td>')
				elif (len(name.cssselect('.content-test')[0].cssselect('p')) > 0):
					newList2 = name.cssselect('.content-test')[0].cssselect('p')
					f.write('<td>')
					for paragraph in newList2:
						f.write(clearStr(paragraph.text))
						f.write('<br>')
					f.write('</td>')
				elif (len(name.cssselect('.content-test')[0].cssselect('.progress-info .progress-info')) > 0):
					f.write('<td>')
					f.write(clearStr(name.cssselect('.content-test')[0].cssselect('.progress-info .progress-info')[0].text))
					f.write('</td>')
				elif (len(name.cssselect('.content-test')[0].cssselect('span')) > 0) or ('Системы статистики' in name.cssselect('.info-test')[0].text):
					f.write('<td>')
					newList2 = name.cssselect('.content-test')[0].cssselect('span')
					for analytics in newList2:
						f.write(clearStr(analytics.text))
						f.write('<br>')
					f.write('</td>')
				elif (len(name.cssselect('.content-test')[0].cssselect('.progress-info')) > 0):
					f.write('<td>')
					f.write(clearStr(name.cssselect('.content-test')[0].cssselect('.progress-info')[0].text))
					f.write('</td>')
			except:
				pass
		i += 1
		f.write('<td>')
		newList3 = name.cssselect('.description p')
		for paragraph in newList3:
			f.write(paragraph.text)
		f.write('</td></tr>')
		#f.write('\n')
	except Exception:
		#set_trace()
		f.write('</td></tr>')
		#f.write('\n')
		pass
print(i)
f.write('</table>')
f.write('''
</body>
</html>
	''')
f.close()
'''
for name in newList:
	newVar = name.text
	set_trace()
	newVar = newVar.replace('\n','')
	newVar = newVar.replace('\t','')
	newVar = newVar.replace('\r','')
	print(newVar)
'''
