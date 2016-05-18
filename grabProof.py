from grab import Grab
from ipdb import set_trace

g = Grab()

g.go('https://id.pr-cy.ru/signup/login/')

g.doc.set_input('login_email','neo@biksileev.ru') 
g.doc.set_input('password','biksileev')
g.doc.submit()
g.go('https://a.pr-cy.ru/biksileev.ru')

newList = g.css_list('.row')

i = 0

for name in newList[5:]:
	try:
		'''if 'Системы статистики' in name.cssselect('.info-test')[0].text:
			set_trace()'''
		if not('Обратные ссылки' in name.cssselect('.info-test')[0].text):
			print(name.cssselect('.info-test')[0].text, end=' ')
			try:
				newVar = name.cssselect('.content-test')[0].text
				newVar = newVar.replace('\n','')
				newVar = newVar.replace('\t','')
				newVar = newVar.replace('\r','')
				if len(newVar) > 0:
					print(newVar)
				else:
					try:
						newVar2 = name.cssselect('.content-test')[0].cssselect('a')[0].text
						newVar2 = newVar.replace('\n','')
						newVar2 = newVar.replace('\t','')
						newVar2 = newVar.replace('\r','')
					except:
						try:
							print(name.cssselect('.content-test')[0].cssselect('p')[0].text, end=' ')
						except:
							try:
								print(name.cssselect('.content-test')[0].cssselect('p')[0].text, end=' ')
							except:
								try:
									print(name.cssselect('.content-test')[0].cssselect('.progress-info .progress-info')[0].text)
								except:
									try:
										newList2 = name.cssselect('.content-test')[0].cssselect('span')
										for analytics in newList2:
											print(analytics.text, end=' ')
									except:
										pass
					'''if len(newVar2) > 0:
							print(newVar2)
						else:
							print(name.cssselect('.content-test')[0].cssselect('p')[0].text, end=' ')'''
			except:
				pass
		i += 1
		print()
	except:
		pass
print(i)
'''
for name in newList:
	newVar = name.text
	set_trace()
	newVar = newVar.replace('\n','')
	newVar = newVar.replace('\t','')
	newVar = newVar.replace('\r','')
	print(newVar)
'''
