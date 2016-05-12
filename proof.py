import requests
import urllib.parse
import time

methods = ('reindex_site', 'get_index')

sites = ('biksileev.ru', 'marvel-gold.ru', 'atl96.ru')

BASE_URL = 'http://api.megaindex.ru/?'

paramsForReIndex = {
	'method': methods[0],
	'output': 'json',
	'mode': 'site',
	'login': 'dmitriy@biksileev.ru',
	'password': 'NokiaN9777',
	'url': sites[1],
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

print(secondJson)