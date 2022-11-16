import tkinter as tk
from tkinter import filedialog, Text , ttk
import os


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

    sysID = 10000000 # fix so no duplicate after reboot #a

    def __init__(self):
        self.searchBy = 0
        self.sortBy = 0
        self.employees = []
        self.load()
        self.currentEmployeeList = self.employees

    def load(self):
        if os.path.isfile('save.txt'):
            with open('save.txt') as save:
                empList = save.read()
                empList = empList.split('<>')
                #print(empList)
                if len(empList) > 1:
                    for emp in empList:
                        data = emp.split(';;')
                        if len(data) > 9:
                            noteString = data[9]
                            notesStrip = noteString[1: len(noteString) -1]
                            notesStrip = notesStrip.replace("'", "")
                            print(notesStrip)
                            newEmp = employee(data[0], data[1], data[2], data[3], data[4],
                                data[5], data[6], data[7], data[8], notesStrip.split(','))
                            self.employees.append(newEmp) #add

    #def checkAccess(self):

    def search(self, by, criteria):
        searchResults = []
        if by == 0:
            by = -1
        for e in self.employees:
            if e.info[by+1] == criteria:
                searchResults.append(e)
        self.currentEmployeeList = searchResults
        self.showEmployees(searchResults)

    def sort(self, by):
        if by == 7:
            self.currentEmployeeList = self.employees
        else:
            if by == 0:
                by = -1
            def searchHelper(e):
                print(e.info[by+1])
                return e.info[by+1]
            self.currentEmployeeList.sort(key=searchHelper)
        self.showEmployees(self.currentEmployeeList)

    def save(self):
        if len(self.employees) > 0:
            with open('save.txt', 'w') as save:
                for employee in self.employees:
                    save.write(employee.show() + '<>') #add

    def showEmployees(self, results):
        for widget in canvas.winfo_children():
            widget.destroy()

        lbox = tk.Listbox(canvas, width = 100, selectmode=tk.SINGLE)
        lbox.pack()

        for i in range(len(results)):
            lbox.insert(i, results[i].show())

        empframe = tk.Frame(canvas, width = 700)
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

    def newNote(self, index): #add
        noteWindow = tk.Tk()

        noteToAdd = tk.Entry(noteWindow, bd =5,)
        noteToAdd.pack()
        def noteHelper():
            self.currentEmployeeList[index].addNote(noteToAdd.get())
            noteWindow.destroy()
            self.showEmployees(self.currentEmployeeList)
        add = tk.Button(noteWindow, text="Save Note", bd=5, command= noteHelper)
        add.pack()
        noteWindow.mainloop()

    def addEmployee(self):
        addEmp = tk.Tk()
        #addCanvas = tk.Canvas(addEmp, height=200, width =200, bg="white")
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
        def addHelper():
            newEmployee = employee(system.sysID, password.get(),
            fName.get(), lName.get(), occ.get(), lvl.get(), past.get(), exp.get(), contactInformation.get(), [])

            print(newEmployee.show())
            print(passW)
            print(last)
            self.employees.append(newEmployee)

            self.incrementID()
            addEmp.destroy()
            self.showEmployees(self.employees) #add

        #press = lambda self: self.addHelper(password.get(),
        #fName.get(), lName.get(), occ.get(), lvl.get(), past.get(), exp.get(), contactInformation.get())
        #add = tk.Button(addEmp, text="Add", bd=5, command=  lambda: press(self))
        add = tk.Button(addEmp, text="Add", bd=5, command= addHelper)

        add.pack()
        addEmp.mainloop()

    @classmethod
    def incrementID(cls):
        cls.sysID += 1

    def removeEmployee(self,index):
        self.employees.remove(self.currentEmployeeList.pop(index))
        self.showEmployees(self.currentEmployeeList)

    def updateEmployee(self,index):
        addEmp = tk.Tk()

        password = tk.Entry(addEmp, bd =5,)
        password.pack()
        password.insert(0, self.currentEmployeeList[index].getPassword())

        fName = tk.Entry(addEmp, bd =5)
        fName.pack()
        fName.insert(0, self.currentEmployeeList[index].getFirstName())

        lName = tk.Entry(addEmp, bd =5)
        lName.pack()
        lName.insert(0, self.currentEmployeeList[index].getLastName())

        occ = tk.Entry(addEmp, bd =5)
        occ.pack()
        occ.insert(0, self.currentEmployeeList[index].getOccupation())

        lvl = tk.Entry(addEmp, bd =5)
        lvl.pack()
        lvl.insert(0, self.currentEmployeeList[index].getLevel())

        past = tk.Entry(addEmp, bd =5)
        past.pack()
        past.insert(0, self.currentEmployeeList[index].getPastExperience())

        exp = tk.Entry(addEmp, bd =5)
        exp.pack()
        exp.insert(0, self.currentEmployeeList[index].getTimeInPos())

        contactInformation = tk.Entry(addEmp, bd =5)
        contactInformation.pack()
        contactInformation.insert(0, self.currentEmployeeList[index].getContactInfo())

        def updateHelper():
            self.currentEmployeeList[index].setPassword(password.get())
            self.currentEmployeeList[index].setFirstName(fName.get())
            self.currentEmployeeList[index].setLastName(lName.get())
            self.currentEmployeeList[index].setOccupation(occ.get())
            self.currentEmployeeList[index].setLevel(lvl.get())
            self.currentEmployeeList[index].setPastExperience(past.get())
            self.currentEmployeeList[index].setTimeInPos(exp.get())
            self.currentEmployeeList[index].setContactInfo(contactInformation.get())
            self.showEmployees(self.employees)
            addEmp.destroy()

        add = tk.Button(addEmp, text="Update", bd=5, command= updateHelper)
        add.pack()
        addEmp.mainloop()


sys = system()
#sys.load()
root = tk.Tk()
searchFrame = tk.Frame(root, borderwidth=10)
searchFrame.pack()
canvas = tk.Canvas(root, height=700, width =700, bg="white")
canvas.pack()

sortVar = ttk.Combobox(searchFrame, text="Sort", width = 3)
sortVar['values'] = ['ID', 'First Name', 'Last Name', 'Job Title', 'Level',
                        'Past Experience','Time in Role', 'Show All']
sortVar.bind('<<ComboboxSelected>>', lambda x: sys.sort(sortVar.current()))
sortVar.set("Sort")
sortVar.pack(side ="right")

searchBar = tk.Entry(searchFrame, width = 15, bd =5)
searchButton = tk.Button(searchFrame, text="Search",width = 4, bg="black",
                command=lambda:sys.search(searchVar.current(), searchBar.get()))


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

add = tk.Button(root, text="Add Employee", padx=10,pady=5, bg="black", command=sys.addEmployee)
add.pack()


sys.showEmployees(sys.employees)
root.mainloop()
sys.save()
