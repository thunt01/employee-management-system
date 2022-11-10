import tkinter as tk
from tkinter import filedialog, Text
import os
from functools import partial





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

    def show(self):
        employeeTxt = ','.join(str(x) for x in self.info)
        return employeeTxt

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
        #print(type(self.info[9]))


class system:

    sysID = 10000000 # fix so no duplicate after reboot

    def __init__(self):
        self.searchBy = 0
        self.sortBy = 0
        self.employees = []
        self.load()

    def load(self):
        if os.path.isfile('save.txt'):
            with open('save.txt') as save:
                empList = save.read()
                empList = empList.split(';')
                #print(empList)
                if len(empList) > 1:
                    for emp in empList:
                        data = emp.split(',')
                        if len(data) == 10:
                            noteString = data[9]
                            notesStrip = noteString[1: len(noteString) -1]
                            newEmp = employee(data[0], data[1], data[2], data[3], data[4],
                                data[5], data[6], data[7], data[8], notesStrip.split(','))
                            self.employees.append(newEmp)

    #def checkAccess(self):

    #def search(): employee[]

    #def sort(): employee[]

    def save(self):
        if len(self.employees) > 0:
            with open('save.txt', 'w') as save:
                for employee in self.employees:
                    save.write(employee.show() + ';')

    def showEmployees(self):
        for widget in canvas.winfo_children():
            widget.destroy()

        lbox = tk.Listbox(canvas, selectmode=tk.SINGLE)
        lbox.pack()

        for i in range(len(self.employees)):
            lbox.insert(i, self.employees[i].show())

        empframe = tk.Frame(canvas, borderwidth=10)
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

    def newNote(self, index):
        noteWindow = tk.Tk()

        noteToAdd = tk.Entry(noteWindow, bd =5,)
        noteToAdd.pack()
        def noteHelper():
            self.employees[index].addNote(noteToAdd.get())
            self.showEmployees()
            noteWindow.destroy()
        add = tk.Button(noteWindow, text="Save Note", bd=5, command= noteHelper)
        add.pack()
        noteWindow.mainloop()

    def addEmployee(self):
        addEmp = tk.Tk()
        addCanvas = tk.Canvas(addEmp, height=200, width =200, bg="white")
        canvas.pack()
        password = tk.Entry(addEmp, bd =5,)
        password.pack()
        passW = password.get()
        fName = tk.Entry(addEmp, bd =5)
        fName.pack()
        first = fName.get()
        lName = tk.Entry(addEmp, bd =5)
        lName.pack()
        last = lName.get()
        occ = tk.Entry(addEmp, bd =5)
        occ.pack()
        occupation = occ.get()
        lvl = tk.Entry(addEmp, bd =5)
        lvl.pack()
        level = lvl.get()
        past = tk.Entry(addEmp, bd =5)
        past.pack()
        pastXP = past.get()
        exp = tk.Entry(addEmp, bd =5)
        exp.pack()
        xp = exp.get()
        contactInformation = tk.Entry(addEmp, bd =5)
        contactInformation.pack()
        contact = contactInformation.get()
        #print(contact)
        #press = partial(self.addHelper, passW, "fName.get()", last, occupation,level, pastXP, xp ,contact)
        press = lambda self: self.addHelper(password.get(),
        fName.get(), lName.get(), occ.get(), lvl.get(), past.get(), exp.get(), contactInformation.get())
        add = tk.Button(addEmp, text="Add", bd=5, command=  lambda: press(self))
        add.pack()
        addEmp.mainloop()

    @classmethod
    def incrementID(cls):
        cls.sysID += 1

    def addHelper( self, passW, first, last, occ,level, past, xp ,contact):
        newEmployee = employee(system.sysID, passW, first, last, occ,level, past, xp ,contact, [])

        print(newEmployee.show())
        print(passW)
        print(last)
        self.employees.append(newEmployee)

        self.incrementID()
        self.showEmployees()



    def removeEmployee(self,index):
        self.employees.pop(index)
        self.showEmployees()

    def updateEmployee(self,index):
        addEmp = tk.Tk()
        #addCanvas = tk.Canvas(addEmp, height=200, width =200, bg="white")
        #Canvas.pack()

        password = tk.Entry(addEmp, bd =5,)
        password.pack()
        password.insert(0, self.employees[index].getPassword())

        fName = tk.Entry(addEmp, bd =5)
        fName.pack()
        fName.insert(0, self.employees[index].getFirstName())

        lName = tk.Entry(addEmp, bd =5)
        lName.pack()
        lName.insert(0, self.employees[index].getLastName())

        occ = tk.Entry(addEmp, bd =5)
        occ.pack()
        occ.insert(0, self.employees[index].getOccupation())

        lvl = tk.Entry(addEmp, bd =5)
        lvl.pack()
        lvl.insert(0, self.employees[index].getLevel())

        past = tk.Entry(addEmp, bd =5)
        past.pack()
        past.insert(0, self.employees[index].getPastExperience())

        exp = tk.Entry(addEmp, bd =5)
        exp.pack()
        exp.insert(0, self.employees[index].getTimeInPos())

        contactInformation = tk.Entry(addEmp, bd =5)
        contactInformation.pack()
        contactInformation.insert(0, self.employees[index].getContactInfo())

        def updateHelper():
            self.employees[index].setPassword(password.get())
            self.employees[index].setFirstName(fName.get())
            self.employees[index].setLastName(lName.get())
            self.employees[index].setOccupation(occ.get())
            self.employees[index].setLevel(lvl.get())
            self.employees[index].setPastExperience(past.get())
            self.employees[index].setTimeInPos(exp.get())
            self.employees[index].setContactInfo(contactInformation.get())
            self.showEmployees()
            addEmp.destroy()

        add = tk.Button(addEmp, text="Update", bd=5, command= updateHelper)
        add.pack()
        addEmp.mainloop()


sys = system()
#sys.load()
root = tk.Tk()
canvas = tk.Canvas(root, height=700, width =700, bg="white")
canvas.pack()
add = tk.Button(root, text="Add Employee", padx=10,pady=5, bg="black", command=sys.addEmployee)
add.pack()


sys.showEmployees()
root.mainloop()
sys.save()
