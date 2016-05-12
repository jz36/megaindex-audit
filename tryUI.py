from tkinter import *
import requests
import urllib.parse
import time

def idexSite(site):
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

	time.sleep(600)

	secondResponse = requests.get(BASE_URL, params=paramsForGetIndex)
	secondJson = secondResponse.json()

	return secondJson

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

mainFrame.pack()

nameLabel.pack()

nameEntry.pack()

siteLabel.pack()

siteEntry.pack()

emailLabel.pack()

emailEntry.pack()

buttonSend.pack()

root.mainloop()
