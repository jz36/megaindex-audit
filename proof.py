import requests
import urllib.parse
import time
from requests.auth import HTTPDigestAuth

'''methods = ('reindex_site', 'get_index')

sites = ('biksileev.ru', 'marvel-gold.ru', 'atl96.ru')

BASE_URL = 'http://api.megaindex.ru/?'

paramsForReIndex = {
	'method': methods[0],
	'output': 'json',
	'mode': 'site',
	'login': 'dmitriy@biksileev.ru',
	'password': 'NokiaN9777',
	'url': sites[2],
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
	'url': paramsForReIndex['url'],
	'version_id': firstJson['version_id']
}

time.sleep(600)

secondResponse = requests.get(BASE_URL, params=paramsForGetIndex)
secondJson = secondResponse.json()

print(secondJson)'''

session = requests.Session()
session.post('https://id.pr-cy.ru/signup/login/', {
     'login_email': 'neo@biksileev.ru',
     'password': 'biksileev',
     'remember': 1,
})


BASE_URL = 'https://a.pr-cy.ru'

response = requests.get('https://id.pr-cy.ru/signup/login/')

print('Яндекс' in response.text)

f = open('test.html', 'w', encoding='ISO-8859-1')

#msg = str(response.text).encode('cp1251')

f.write(str(response.text))

f.close()