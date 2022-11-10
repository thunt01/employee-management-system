import tkinker as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width =700, bg="white")
canvas.pack()




with open('save.txt', 'w') as save:
    for employee in employees:
        save.write(employee.show() + ';')

class employee():
    def __init__(self, id, pass, first, last, occ, level, past, xp ,contact, note):
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
        info = []
        notes = []
        notes.append(note)

        self.info.append(id)
        self.info.append(pass)
        self.info.append(first)
        self.info.append(last)
        self.info.append(occ)
        self.info.append(level)
        self.info.append(past)
        self.info.append(xp)
        self.info.append(contact)
        self.info.append(notes)

        #add
    def updateAll(self, pass, first, last, occ, level, past, xp ,contact):
        #self.password = pass
        #self.firstName = first
        #self.lastName = last
        #self.occupation = occ
        #self.level = level
        #self.pastExperience = past
        #self.timeInPos = xp
        #self.contactInfo: = contact
        self.info[1] = pass
        self.info[2] = first
        self.info[3] = last
        self.info[4] = occ
        self.info[5] = level
        self.info[6] = past
        self.info[7] = xp
        self.info[8] = contact

    def show(self):
        employeeTxt = self.info[0]
        for i in range(8):
            employeeText = employeeTxt + ',' + self.info[i+1]
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

    def setPassword(self, pass):
        self.password = pass

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



class system():
    def __init__(self):
        searchBy = 0
        sortBy = 0
        employees = []
        if os.path.isfile('save.txt'):
            with open('save.txt') as save:
                empList = save.read()
                empList = empList.split(';')
                for emp in empList:
                    data = emp.split(',')
                    self.employees.append(employee(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8] data[9])

    def checkAccess(self):

    def search(): employee[]

    def sort(): employee[]

    def showEmployees(self)
        print(employees) #adapt to gui

    def addEmployee(self, employee):
        employees.append(employee)

    def removeEmployee(): void

    def updateEmployee(): void
