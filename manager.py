import tkinter as tk
from tkinter import filedialog, Text , ttk
from tkinter import *
import os
#from login import *


class employee:
    def __init__(self, id, passW, first, last, occ, level, past, xp ,contact, note):
        #self.id = id
        #self.password = pass
        #self.firstName = first
        #self.lastName = last
        #self.occupation = occ
        #self.level = level
        #self.pastExperience = past
        #self.timeInPos = xp
        #self.contactInfo: = contact
        #self.notes = [note] #double check
        self.info = []
        notes = note

        self.info.append(id)
        self.info.append(passW)
        self.info.append(first)
        self.info.append(last)
        self.info.append(occ)
        self.info.append(level)
        self.info.append(past)
        self.info.append(xp)
        self.info.append(contact)
        self.info.append(notes)

        #add
    def updateAll(self, passW, first, last, occ, level, past, xp ,contact):
        #self.password = pass
        #self.firstName = first
        #self.lastName = last
        #self.occupation = occ
        #self.level = level
        #self.pastExperience = past
        #self.timeInPos = xp
        #self.contactInfo: = contact
        self.info[1] = passW
        self.info[2] = first
        self.info[3] = last
        self.info[4] = occ
        self.info[5] = level
        self.info[6] = past
        self.info[7] = xp
        self.info[8] = contact

    def show(self):#add
        employeeTxt = ';;'.join(str(x) for x in self.info[0:9])
        noteToString = ','.join(str(y) for y in self.info[9])
        employeeTxt = employeeTxt + ';;'+ '[' + noteToString + ']'
        return employeeTxt.replace("'", "")

    def getID(self):
        return self.info[0]

    def getPassword(self):
        return self.info[1]

    def getFirstName(self):
        return self.info[2]

    def getLastName(self):
        return self.info[3]

    def getOccupation(self):
        return self.info[4]

    def getLevel(self):
        return self.info[5]

    def getPastExperience(self):
        return self.info[6]

    def getTimeInPos(self):
        return self.info[7]

    def getContactInfo(self):
        return self.info[8]

    def getNotes(self):
        return self.info[9]

    def setID(self,id):
        self.info[0] = id

    def setPassword(self, passW):
        self.info[1] = passW

    def setFirstName(self, fName):
        self.info[2] = fName

    def setLastName(self,lName):
        self.info[3] = lName

    def setOccupation(self, occ):
        self.info[4] = occ

    def setLevel(self,level):
        self.info[5] = level

    def setPastExperience(self,pastXP):
        self.info[6] = pastXP

    def setTimeInPos(self,xp):
        self.info[7] = xp

    def setContactInfo(self,contact):
        self.info[8] = contact

    def addNote(self,note):
        self.info[9].append(note)


class system:

     #sysID = 10000000# fix so no duplicate after reboot #a

    def __init__(self):
        #self.searchBy = 0
        #self.sortBy = 0

        self.sysID = 10000000
        self.employees = []
        self.load()
        self.currentEmployeeList = self.employees
        self.root = tk.Tk()
        searchFrame = tk.Frame(self.root, borderwidth=10)
        searchFrame.pack()
        self.canvas = tk.Canvas(self.root, height=700, width =700 ) #, bg="black")
        self.canvas.pack()

        sortVar = ttk.Combobox(searchFrame, text="Sort", width = 3)
        sortVar['values'] = ['ID', 'First Name', 'Last Name', 'Job Title', 'Level',
                                'Past Experience','Time in Role', 'Show All']
        sortVar.bind('<<ComboboxSelected>>', lambda x: self.sort(sortVar.current()))

        sortVar.set("Sort")
        sortVar.pack(side ="right")

        searchBar = tk.Entry(searchFrame, width = 15, bd =5)
        searchButton = tk.Button(searchFrame, text="Search",width = 4, bg="black",
                        command=lambda: self.search(searchVar.current(), searchBar.get()))


        searchVar = ttk.Combobox(searchFrame, text="Search By", width = 7)
        searchVar.pack(side ="left")
        searchVar['values'] = ['ID', 'First Name', 'Last Name', 'Job Title', 'Level',
                                'Past Experience','Time in Role']
        searchVar.set("Search By")


        searchButton.pack(side ="right")
        searchBar.pack(side ="right")


        if searchVar.current() == -1:
            searchBar['state'] = 'disabled'
        def searchAble(self):
            searchBar['state'] = 'normal'
        searchVar.bind('<<ComboboxSelected>>', searchAble)

        add = tk.Button(self.root, text="Add Employee", padx=10,pady=5,bd = 5, bg="black", command=self.addEmployee)
        add.pack()

        self.showEmployees(self.employees)
        self.root.mainloop()
        self.save()


    def load(self):
        if os.path.isfile('save.txt'):
            with open('save.txt') as save:
                txtList = save.read()
                txtList = txtList.split('<>')

                #print(empList)
                if len(txtList) > 1:
                    self.sysID = int(txtList[len(txtList)-1])

                    empList = txtList[0: len(txtList) - 1]

                    for emp in empList:
                        data = emp.split(';;')
                        if len(data) > 9:
                            noteString = data[9]
                            notesStrip = noteString[1: len(noteString) -1]
                            notesStrip = notesStrip.replace("'", "")
                            #print(notesStrip)
                            newEmp = employee(int(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]),
                                int(data[5]), int(data[6]), int(data[7]), str(data[8]), notesStrip.split(','))
                            self.employees.append(newEmp) #add

    #def checkAccess(self):
        #return self.log.auth

    def search(self, by, criteria):
        searchResults = []
        if by == 0:
            by = -1
        if by > 3:
            for e in self.employees:
                if int(e.info[by+1]) > int(criteria)-1:
                    searchResults.append(e)
        else:
            for e in self.employees:
                if criteria.lower() in e.info[by+1].lower():
                    searchResults.append(e)
        self.currentEmployeeList = searchResults
        self.showEmployees(searchResults)

    def sort(self, by):
        if by == 7:
            self.currentEmployeeList = self.employees
        else:
            if by == 0:
                by = -1
            def sortHelper(e):
                #print(e.info[by+1])
                return e.info[by+1]
            self.currentEmployeeList.sort(key=sortHelper)
        self.showEmployees(self.currentEmployeeList)

    def save(self):
        if len(self.employees) > 0:
            with open('save.txt', 'w') as save:
                for employee in self.employees:
                    save.write(employee.show() + '<>') #add
                save.write(str(self.sysID))

    def showEmployees(self, results):

        for widget in self.canvas.winfo_children():
            widget.destroy()

        lbox = tk.Listbox(self.canvas, width = 35, bd=5, selectmode=tk.SINGLE)
        lbox.pack()

        for i in range(len(results)):
            #lbox.insert(i, results[i].show())
            lbox.insert(i, str(results[i].getID()) +": "+ results[i].getFirstName() + " "
            + results[i].getLastName() + ", " + results[i].getOccupation())

        empframe = tk.Frame(self.canvas, width = 700)
        empframe.pack()
        delete = tk.Button(empframe, text="Delete", state= 'disabled', padx=10,pady=5, bg="gray",
        command= lambda: self.removeEmployee(lbox.curselection()[0]))
        delete.pack(side = "right")
        update = tk.Button(empframe, text="Update",state= 'disabled', padx=10,pady=5, bg="gray",
        command = lambda: self.updateEmployee(lbox.curselection()[0]))
        update.pack(side = "right")
        addNote = tk.Button(empframe, text="Add Note",state= 'disabled', padx=10,pady=5, bg="gray",
        command = lambda: self.newNote(lbox.curselection()[0]))
        addNote.pack(side = "right")

        def enable(self):
            delete['state'] = 'normal'
            update['state'] = 'normal'
            addNote['state'] = 'normal'
        lbox.bind('<<ListboxSelect>>', enable)
        lbox.bind('<Double-Button-1>',  lambda x: self.viewEmployee(lbox.curselection()[0]))

    def viewEmployee(self, index):
        viewE = tk.Toplevel()
        view = tk.Frame(viewE, bd=5)
        view.pack()

        eID = tk.Label(view, text = ' Employee: '+ str(self.currentEmployeeList[index].getID()),
                                    font='Helvetica 18 bold')
        eID.pack()

        fName = tk.Label(view, text = ' First Name: '+ str(self.currentEmployeeList[index].getFirstName()))
        fName.pack()

        lName = tk.Label(view, text = ' Last Name: '+ str(self.currentEmployeeList[index].getLastName()))
        lName.pack()

        occ = tk.Label(view, text = ' Job Title: '+ str(self.currentEmployeeList[index].getOccupation()))
        occ.pack()

        lvl = tk.Label(view, text = ' Level: '+ str(self.currentEmployeeList[index].getLevel()))
        lvl.pack()

        past = tk.Label(view, text = ' Past Experience: '+ str(self.currentEmployeeList[index].getPastExperience()) + ' years')
        past.pack()

        exp = tk.Label(view, text = ' Time in Position: '+ str(self.currentEmployeeList[index].getTimeInPos()) + ' years')
        exp.pack()

        contactInformation = tk.Label(view, text = ' Contact Information: '+ str(self.currentEmployeeList[index].getContactInfo()))
        contactInformation.pack()

        employeeNotes = self.currentEmployeeList[index].getNotes()

        noteLabel = tk.Label(view, text = 'Notes:')
        noteLabel.pack()
        i = 1
        for n in employeeNotes:
            if n.strip():
                eNote = tk.Label(view, text = str(i) + '. ' + n)
                i +=1
                eNote.pack()
        #notes

    def newNote(self, index): #add
        noteWindow = tk.Toplevel()

        noteToAdd = tk.Entry(noteWindow, bd =5,)
        noteToAdd.pack()

        errorLabel = tk.Label(noteWindow, text = '')
        errorLabel.pack()

        def noteHelper():
            input = noteToAdd.get().strip()
            if input:
                self.currentEmployeeList[index].addNote(input)
                noteWindow.destroy()
                self.showEmployees(self.currentEmployeeList)
            else:
                errorLabel['text'] = 'Missing Data: Please Enter A Note'
                errorLabel['fg'] = 'red'

        addButton = tk.Button(noteWindow, text="Save Note", command= noteHelper)
        addButton.pack()
        noteWindow.mainloop()

    def addEmployee(self):
        addEmp = tk.Toplevel()

        passFrame = tk.Frame(addEmp, borderwidth=10)
        passFrame.pack()
        passLabel = tk.Label(passFrame, text = ' Password: ')
        passLabel.pack(side = 'left')
        password = tk.Entry(passFrame, bd =5,)
        password.pack(side = 'right')

        fFrame = tk.Frame(addEmp, borderwidth=10)
        fFrame.pack()
        fLabel = tk.Label(fFrame, text = ' First Name: ')
        fLabel.pack(side = 'left')
        fName = tk.Entry(fFrame, bd =5)
        fName.pack(side = 'right')

        lFrame = tk.Frame(addEmp, borderwidth=10)
        lFrame.pack()
        lLabel = tk.Label(lFrame, text = 'Last Name:')
        lLabel.pack(side = 'left')
        lName = tk.Entry(lFrame, bd =5)
        lName.pack(side = 'right')

        occFrame = tk.Frame(addEmp, borderwidth=10)
        occFrame.pack()
        occLabel = tk.Label(occFrame, text = 'Job Title:')
        occLabel.pack(side = 'left')
        occ = tk.Entry(occFrame, bd =5)
        occ.pack(side = 'right')

        lvlFrame = tk.Frame(addEmp, borderwidth=10)
        lvlFrame.pack()
        lvlLabel = tk.Label(lvlFrame, text = 'Level:')
        lvlLabel.pack(side = 'left')
        lvl = tk.Entry(lvlFrame, bd =5)
        lvl.pack(side = 'right')

        pastFrame = tk.Frame(addEmp, borderwidth=10)
        pastFrame.pack()
        pastLabel = tk.Label(pastFrame, text = 'Past Experience:')
        pastLabel.pack(side = 'left')
        past = tk.Entry(pastFrame, bd =5)
        past.pack(side = 'right')

        expFrame = tk.Frame(addEmp, borderwidth=10)
        expFrame.pack()
        expLabel = tk.Label(expFrame, text = 'Time in Position:')
        expLabel.pack(side = 'left')
        exp = tk.Entry(expFrame, bd =5)
        exp.pack(side = 'right')

        conFrame = tk.Frame(addEmp, borderwidth=10)
        conFrame.pack()
        conLabel = tk.Label(conFrame, text = 'Contact Info:')
        conLabel.pack(side = 'left')
        contactInformation = tk.Entry(conFrame, bd =5)
        contactInformation.pack(side = 'right')

        errorFrame = tk.Frame(addEmp, borderwidth=10)
        errorFrame.pack()
        errorLabel = tk.Label(errorFrame, text = '')
        errorLabel.pack()
        def addHelper():
            valid = True
            try:
                intLevel = int(lvl.get())
                lvlLabel['fg'] = 'white'
            except ValueError:
                errorLabel['text'] = 'Invalid Input: Please Enter A Number'
                errorLabel['fg'] = 'red'
                lvlLabel['fg'] = 'red'
                valid = False
            try:
                intPast = int(past.get())
                pastLabel['fg'] = 'white'
            except ValueError:
                errorLabel['text'] = 'Invalid Input: Please Enter A Number'
                errorLabel['fg'] = 'red'
                pastLabel['fg'] = 'red'
                valid = False
            try:
                intExp = int(exp.get())
                expLabel['fg'] = 'white'
            except ValueError:
                errorLabel['text'] = 'Invalid Input: Please Enter A Number'
                errorLabel['fg'] = 'red'
                expLabel['fg'] = 'red'
                valid = False
            passW = str(password.get().strip())
            first = str(fName.get().strip())
            last = str(lName.get().strip())
            title = str(occ.get().strip())
            cInfo = str(contactInformation.get().strip())
            if passW and first and last and title and cInfo:
                if valid:
                    newEmployee = employee(self.sysID, passW, first,
                        last, title, intLevel, intPast,
                        intExp, cInfo, [])

                    print(newEmployee.show())

                    self.employees.append(newEmployee)
                    self.currentEmployeeList = self.employees

                    self.incrementID()
                    addEmp.destroy()
                    self.showEmployees(self.employees)
            else:
                errorLabel['text'] = 'Missing Data: Please Complete All Fields'
                errorLabel['fg'] = 'red'
                pastLabel['fg'] = 'white'
                expLabel['fg'] = 'white'
                lvlLabel['fg'] = 'white'


             #add

        add = tk.Button(addEmp, text="Add", bd=5, command= addHelper)
        add.pack()
        addEmp.mainloop()

    #@classmethod
    def incrementID(self):
        self.sysID += 1

    def removeEmployee(self,index):
        self.employees.remove(self.currentEmployeeList[index])
        #self.currentEmployeeList.pop(index)
        self.showEmployees(self.employees)

    def updateEmployee(self,index):
        addEmp = tk.Toplevel()

        passFrame = tk.Frame(addEmp, borderwidth=10)
        passFrame.pack()
        passLabel = tk.Label(passFrame, text = ' Password: ')
        passLabel.pack(side = 'left')
        password = tk.Entry(passFrame, bd =5,)
        password.pack(side = 'right')
        password.insert(0, self.currentEmployeeList[index].getPassword())


        fFrame = tk.Frame(addEmp, borderwidth=10)
        fFrame.pack()
        fLabel = tk.Label(fFrame, text = ' First Name: ')
        fLabel.pack(side = 'left')
        fName = tk.Entry(fFrame, bd =5)
        fName.pack(side = 'right')
        fName.insert(0, self.currentEmployeeList[index].getFirstName())

        lFrame = tk.Frame(addEmp, borderwidth=10)
        lFrame.pack()
        lLabel = tk.Label(lFrame, text = 'Last Name:')
        lLabel.pack(side = 'left')
        lName = tk.Entry(lFrame, bd =5)
        lName.pack(side = 'right')
        lName.insert(0, self.currentEmployeeList[index].getLastName())

        occFrame = tk.Frame(addEmp, borderwidth=10)
        occFrame.pack()
        occLabel = tk.Label(occFrame, text = 'Job Title:')
        occLabel.pack(side = 'left')
        occ = tk.Entry(occFrame, bd =5)
        occ.pack(side = 'right')
        occ.insert(0, self.currentEmployeeList[index].getOccupation())

        lvlFrame = tk.Frame(addEmp, borderwidth=10)
        lvlFrame.pack()
        lvlLabel = tk.Label(lvlFrame, text = 'Level:')
        lvlLabel.pack(side = 'left')
        lvl = tk.Entry(lvlFrame, bd =5)
        lvl.pack(side = 'right')
        lvl.insert(0, self.currentEmployeeList[index].getLevel())

        pastFrame = tk.Frame(addEmp, borderwidth=10)
        pastFrame.pack()
        pastLabel = tk.Label(pastFrame, text = 'Past Experience:')
        pastLabel.pack(side = 'left')
        past = tk.Entry(pastFrame, bd =5)
        past.pack(side = 'right')
        past.insert(0, self.currentEmployeeList[index].getPastExperience())

        expFrame = tk.Frame(addEmp, borderwidth=10)
        expFrame.pack()
        expLabel = tk.Label(expFrame, text = 'Time in Position:')
        expLabel.pack(side = 'left')
        exp = tk.Entry(expFrame, bd =5)
        exp.pack(side = 'right')
        exp.insert(0, self.currentEmployeeList[index].getTimeInPos())

        conFrame = tk.Frame(addEmp, borderwidth=10)
        conFrame.pack()
        conLabel = tk.Label(conFrame, text = 'Contact Info:')
        conLabel.pack(side = 'left')
        contactInformation = tk.Entry(conFrame, bd =5)
        contactInformation.pack(side = 'right')
        contactInformation.insert(0, self.currentEmployeeList[index].getContactInfo())

        errorFrame = tk.Frame(addEmp, borderwidth=10)
        errorFrame.pack()
        errorLabel = tk.Label(errorFrame, text = '')
        errorLabel.pack()

        def updateHelper():
            #print("hello")
            valid = True

            try:
                intLevel = int(lvl.get())
                lvlLabel['fg'] = 'white'
            except ValueError:
                errorLabel['text'] = 'Invalid Input: Please Enter A Number'
                errorLabel['fg'] = 'red'
                lvlLabel['fg'] = 'red'
                valid = False
            try:
                intPast = int(past.get())
                pastLabel['fg'] = 'white'
            except ValueError:
                errorLabel['text'] = 'Invalid Input: Please Enter A Number'
                errorLabel['fg'] = 'red'
                pastLabel['fg'] = 'red'
                valid = False
            try:
                intExp = int(exp.get())
                expLabel['fg'] = 'white'
            except ValueError:
                errorLabel['text'] = 'Invalid Input: Please Enter A Number'
                errorLabel['fg'] = 'red'
                expLabel['fg'] = 'red'
                valid = False
            passW = str(password.get().strip())
            first = str(fName.get().strip())
            last = str(lName.get().strip())
            title = str(occ.get().strip())
            cInfo = str(contactInformation.get().strip())
            if passW and first and last and title and cInfo:
                if valid:
                    self.currentEmployeeList[index].setPassword(passW)
                    self.currentEmployeeList[index].setFirstName(first)
                    self.currentEmployeeList[index].setLastName(last)
                    self.currentEmployeeList[index].setOccupation(title)
                    self.currentEmployeeList[index].setLevel(intLevel)
                    self.currentEmployeeList[index].setPastExperience(intPast)
                    self.currentEmployeeList[index].setTimeInPos(intExp)
                    self.currentEmployeeList[index].setContactInfo(cInfo)
                    self.showEmployees(self.employees)
                    addEmp.destroy()
            else:
                errorLabel['text'] = 'Missing Data: Please Complete All Fields'
                errorLabel['fg'] = 'red'
                pastLabel['fg'] = 'white'
                expLabel['fg'] = 'white'
                lvlLabel['fg'] = 'white'

        add = tk.Button(addEmp, text="Update", bd=5, command= updateHelper)
        add.pack()
        addEmp.mainloop()

class Authentication:

    #user = 'admin'
    #passw = 'Johnson'

    admins = {
          "admin": "Johnson",
          "ceo": "pass123",
          "cto": "secure"
          }
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('425x185+700+300')

        self.auth = False


        self.root.title('USER AUTHENTICATION')

        '''Make Window 10X10'''

        rows = 0
        while rows<10:
            self.root.rowconfigure(rows, weight=1)
            self.root.columnconfigure(rows, weight=1)
            rows+=1

        '''Username and Password'''

        frame = tk.LabelFrame(self.root, text='Login')
        frame.grid(row = 1,column = 1,columnspan=10,rowspan=10)

        tk.Label(frame, text = ' Username ').grid(row = 2, column = 1, sticky = W)
        self.username = tk.Entry(frame)
        self.username.grid(row = 2,column = 2)

        tk.Label(frame, text = ' Password ').grid(row = 5, column = 1, sticky = W)
        self.password = tk.Entry(frame, show='*')
        self.password.grid(row = 5, column = 2)

        # Button

        tk.Button(frame, text = 'LOGIN',command = self.login_user).grid(row=7,column=2)

        '''Message Display'''
        self.message = Label(text = '',fg = 'Red')
        self.message.grid(row=9,column=6)

        self.root.mainloop()


    def login_user(self):

        '''Check username and password entered are correct'''

        if self.username.get() in self.admins:
            if self.admins[self.username.get()] == self.password.get():
        #if self.username.get() == self.user and self.password.get() == self.passw:


            #Destroy current window
                self.auth = True
                self.root.destroy()



        elif self.username.get().strip() and self.password.get().strip():

            '''Prompt user that either id or password is wrong'''
            self.message['text'] = 'Username or Password incorrect. Try again!'

        else:
            '''Prompt user that either id or password is empty'''
            self.message['text'] = 'Missing Username or Password. Complete All Fields!'


app = Authentication()
#print(app.auth)
if (app.auth):
    sys = system()
