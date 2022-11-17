'''IMporting'''
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import  tkinter.messagebox
from manager import *


class Authentication:

    user = 'admin'
    passw = 'Johnson'
    def __init__(self,root):



        self.root = root
        self.root.title('USER AUTHENTICATION')

        '''Make Window 10X10'''

        rows = 0
        while rows<10:
            self.root.rowconfigure(rows, weight=1)
            self.root.columnconfigure(rows, weight=1)
            rows+=1

        '''Username and Password'''

        frame = LabelFrame(self.root, text='Login')
        frame.grid(row = 1,column = 1,columnspan=10,rowspan=10)

        Label(frame, text = ' Username ').grid(row = 2, column = 1, sticky = W)
        self.username = Entry(frame)
        self.username.grid(row = 2,column = 2)

        Label(frame, text = ' Password ').grid(row = 5, column = 1, sticky = W)
        self.password = Entry(frame, show='*')
        self.password.grid(row = 5, column = 2)

        # Button

        ttk.Button(frame, text = 'LOGIN',command = self.login_user).grid(row=7,column=2)

        '''Message Display'''
        self.message = Label(text = '',fg = 'Red')
        self.message.grid(row=9,column=6)


    def login_user(self):

        '''Check username and password entered are correct'''
        if self.username.get() == self.user and self.password.get() == self.passw:


            # Do the work done by the main of DBMSproject.py

            #Destroy current window
            root.destroy()
            sys = system()
            #Open new window
            #newroot = Tk()
            #application = employee(newroot)
            #newroot.mainloop()



        else:

            '''Prompt user that either id or password is wrong'''
            self.message['text'] = 'Username or Password incorrect. Try again!'













if __name__ == '__main__':

    root = Tk()
    root.geometry('425x185+700+300')
    application = Authentication(root)

    root.mainloop()
