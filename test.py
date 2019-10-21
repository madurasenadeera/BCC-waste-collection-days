#!/usr/bin/env python3

import csv  # allows importing/manipulation/writing of csv files
import tkinter as tk  # GUI


def searchProperty():
    # importing csv information, 'r' denotes the reading of the file
    with open('/Users/madurasenadeera/github/BCC_waste_collection_days/data/Waste Collection Days.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

    # print(csv_reader) # prints object for the imported csv file
    # next(csv_reader)  # steps over initial value ("suburb")

    # for line in csv_reader:
    #    print(line[8])

    # unitQn = input('')

        number = numberEntry.get()
        street = streetEntry.get()
        suburb = suburbEntry.get()

        for line in csv_reader:
            # line[8]:
            if ((line[3] == number) and (line[5] == street.upper()) and (line[8] == suburb.upper())):

                searchLabel["text"] = line[1]

            else:
                #print("Invalid suburb name.")
                pass

###########################
# autocomplete function
###########################


###########################
# Initialising GUI window
###########################


window = tk.Tk()
window.title("BCC Waste Collection")
# window.geometry("800x600")


label = tk.Label(window, text="Waste Collection Day").pack()

suburbLabel = tk.Label(window, text="Suburb").pack()
suburbEntry = tk.Entry(window)
suburbEntry.pack()
streetLabel = tk.Label(window, text="Street").pack()
streetEntry = tk.Entry(window)
streetEntry.pack()
numberLabel = tk.Label(window, text="House number").pack()
numberEntry = tk.Entry(window)
numberEntry.pack()

searchButton = tk.Button(window, text="Search", command=searchProperty).pack()

searchLabel = tk.Label(window)
searchLabel.pack()

frame = tk.Frame(window)
frame.pack()

window.mainloop()
