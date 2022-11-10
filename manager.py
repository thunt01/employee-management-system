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
        #employeeID= str(self.info[0])
        employeeTxt = ','.join(str(x) for x in self.info)
        #for i in range(8):
            #employeeText =+ ',' + str(self.info[i+1])
            #print(employeeTxt)
        return employeeTxt

    def getID(self):
        return self.id

    def getPassword(self):
        return self.password

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getOccupation(self):
        return self.occupation

    def getLevel(self):
        return self.level

    def getPastExperience(self):
        return self.pastExperience

    def getTimeInPos(self):
        return self.timeInPos

    def getContactInfo(self):
        return self.contactInfo

    def getNotes(self):
        return self.notes

    def setID(self,id):
        self.id = id

    def setPassword(self, passW):
        self.password = passW

    def setFirstName(self, fName):
        self.firstName = fName

    def setLastName(self,lName):
        self.lastName = lName

    def setOccupation(self, occ):
        self.occupation = occ

    def setLevel(self,level):
        self.level = level

    def setPastExperience(self,pastXP):
        self.pastExperience = pastXP

    def setTimeInPos(self,xp):
        self.timeInPos = xp

    def setContactInfo(self,contact):
        self.contactInfo = contact

    def addNote(self,note):
        self.notes = note


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
                            newEmp = employee(data[0], data[1], data[2], data[3], data[4],
                                data[5], data[6], data[7], data[8], data[9])
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

        for employee in self.employees: #adapt to gui
            empframe = tk.Frame(canvas, borderwidth=10)
            empframe.pack()
            L = tk.Label(empframe, text= employee.show())
            L.pack()
            delete = tk.Button(empframe, text="Delete", padx=10,pady=5, bg="gray")
            delete.pack(side = "right")
            update = tk.Button(empframe, text="Update", padx=10,pady=5, bg="gray")
            update.pack(side = "right")
            addNote = tk.Button(empframe, text="Note", padx=10,pady=5, bg="gray")
            addNote.pack(side = "right")


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



    #def removeEmployee(): void

    #def updateEmployee(): void
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
