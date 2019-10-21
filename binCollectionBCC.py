#!/usr/bin/env python3

import csv
from tkinter import *

###########################
# CSV data extraction
###########################

suburbList = []
streetList = []
with open('/Users/madurasenadeera/github/BCC_waste_collection_days/data/Waste Collection Days.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for values in csv_reader:
        suburbList.append(values[8])  # compiles column of suburbs into one list
        streetList.append(values[5])

    suburbs = list(dict.fromkeys(suburbList))  # removes duplicate suburbs
    # print(suburbs)  # print list of suburbs
    streets = list(dict.fromkeys(streetList))

lista = suburbs  # IMPORTING SUBURBS
listb = streets

###########################
# FINDING ADDRESS
###########################


def searchProperty():
    # importing csv information, 'r' denotes the reading of the file
    with open('/Users/madurasenadeera/github/BCC_waste_collection_days/data/Waste Collection Days.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        number = numberEntry.get()  # pulling information from GUI entry boxes
        street = streetEntry.get()
        suburb = suburbEntry.get()

        for line in csv_reader:  # for-loop to filter through data from CSV file
            # line[8]:
            # comparing entered info with data
            if ((line[3] == number) and (line[5] == street.upper()) and (line[8] == suburb.upper())):
                searchLabel["text"] = line[1]  # print out bin day info

            else:
                #searchLabel["text"] = "Invalid Address"
                pass  # need to add functionality to tell user that the address is not valid

###########################
# TEXT AUTOCOMPLETE FUNCTION
###########################


class AutocompleteEntry(Entry):
    def __init__(self, lista, *args, **kwargs):

        Entry.__init__(self, *args, **kwargs)
        self.lista = lista
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)

        self.lb_up = False

    def changed(self, name, index, mode):

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:
                if not self.lb_up:
                    self.lb = Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
                    self.lb_up = True

                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END, w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False

    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':
                self.lb.selection_clear(first=index)
                index = str(int(index)-1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:
                self.lb.selection_clear(first=index)
                index = str(int(index)+1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def comparison(self):

        test = self.var.get()  # retreives user inputted information from textbox
        pattern = re.compile('.*' + test.upper() + '.*')  # comparing upper case value
        return [w for w in self.lista if re.match(pattern, w)]


###########################
# TKINTER GUI
###########################

window = Tk()
window.title("BCC Waste Collection")

label = Label(window, text="Waste Collection Day").pack()  # GUI title

# suburb entry box
suburbLabel = Label(window, text="Suburb").pack()
suburbEntry = AutocompleteEntry(lista, window)
suburbEntry.pack()

# street name entry box
streetLabel = Label(window, text="Street").pack()
streetEntry = AutocompleteEntry(listb, window)
streetEntry.pack()

# street number entry box
numberLabel = Label(window, text="House number").pack()
numberEntry = Entry(window)
numberEntry.pack()

# search button
searchButton = Button(window, text="Search", command=searchProperty).pack()

# entry space to displace bin day
searchLabel = Label(window)
searchLabel.pack()

frame = Frame(window)
frame.pack()

window.mainloop()
