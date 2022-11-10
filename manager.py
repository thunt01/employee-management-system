import tkinker as tk
from tkinter import filedialog, Text
import os



root = tk.Tk()
canvas = tk.Canvas(root, height=700, width =700, bg="white")
canvas.pack()
add = tk.button(root, text="Add Employee", padx=10,pady=5, bg="gray")
sys = system()
sys.load()
sys.showEmployees()
root.mainloop()
sys.save()




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
        info = []
        notes = []
        notes.append(note)

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
    def __init__(self):
        self.searchBy = 0
        self.sortBy = 0
        self.employees = []

    def load(self):
        if os.path.isfile('save.txt'):
            with open('save.txt') as save:
                empList = save.read()
                empList = empList.split(';')
                for emp in empList:
                    data = emp.split(',')
                    newEmp = employee(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])
                    self.employees.append(newEmp)

    #def checkAccess(self):

    #def search(): employee[]

    #def sort(): employee[]

    def save(self):
        with open('save.txt', 'w') as save:
            for employee in self.employees:
                save.write(employee.show() + ';')

    def showEmployees(self):
        for employee in self.employees: #adapt to gui
            empframe = tk.Frame(root)
            empframe.pack()
            L = Label(empframe, text= employee.show())
            L.pack()
            delete = tk.button(root, text="Delete", padx=10,pady=5, bg="gray")
            delete.pack(side = RIGHT)
            update = tk.button(root, text="Update", padx=10,pady=5, bg="gray")
            update.pack(side = RIGHT)
            addNote = tk.button(root, text="Note", padx=10,pady=5, bg="gray")
            addNote.pack(side = RIGHT)


    def addEmployee(self, employee):
        employees.append(employee)

    #def removeEmployee(): void

    #def updateEmployee(): void
