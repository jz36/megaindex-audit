from grab import Grab
import ipdb

g = Grab()

g.go('https://id.pr-cy.ru/signup/login/')

g.doc.set_input('login_email','neo@biksileev.ru') 
g.doc.set_input('password','biksileev')
g.doc.submit()
g.go('https://a.pr-cy.ru/biksileev.ru')

newList = g.css_list('.row .col-sm-8')

for name in newList:
	newVar = name.text
	newVar = newVar.replace('\n','')
	newVar = newVar.replace('\t','')
	newVar = newVar.replace('\r','')
	if len(newVar) == 0:
		try:
			if len(name.cssselect('a')) != 0:
				newVar2 = name.cssselect('a')[0].text
			elif len(name.cssselect('.progress-info')) != 0:
				newVar2 = name.cssselect('.progress-info')[0].text
			elif len(name.cssselect('p')) != 0:
				newVar2 = name.cssselect('p')[0].text
			elif len(name.cssselect('.social-group .info')):
				ipdb.set_trace()
				newVar2 = name.cssselect('.social-group .info')[0].cssselect('a b')[0].text
				newVar2 = newVar2.replace('\n','')
				newVar2 = newVar2.replace('\t','')
				newVar2 = newVar2.replace('\r','')
				print (newVar2)
				newVar2 = name.cssselect('.social-group .info')[0].cssselect('p')[0].text
				newVar2 = newVar2.replace('\n','')
				newVar2 = newVar2.replace('\t','')
				newVar2 = newVar2.replace('\r','')
				if len(newVar2) == 0:
					newVar2 = name.cssselect('.social-group .info')[0].cssselect('p span')[0].text
					newVar2 = newVar2.replace('\n','')
					newVar2 = newVar2.replace('\t','')
					newVar2 = newVar2.replace('\r','')
					print(newVar2)
					newVar2 = name.cssselect('.social-group .info')[0].cssselect('p span')[1].text
					newVar2 = newVar2.replace('\n','')
					newVar2 = newVar2.replace('\t','')
					newVar2 = newVar2.replace('\r','')
				print (newVar2)


			newVar2 = newVar2.replace('\n','')
			newVar2 = newVar2.replace('\t','')
			newVar2 = newVar2.replace('\r','')
			print(newVar2)
		except:
			print(' ')
	else:
		print(newVar)

