from tkinter import *

root = Tk()

mainFrame = Frame(root, width=250, height=550, bd=5)

nameLabel = Label(mainFrame, text='ФИО клиента:')

nameEntry = Entry(mainFrame)

siteLabel = Label(mainFrame, text='Сайт клиента:')

siteEntry = Entry(mainFrame)

emailLabel = Label(mainFrame, text='E-mail клиента:')

emailEntry = Entry(mainFrame)

'''mainFrame.grid()

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

root.mainloop()
