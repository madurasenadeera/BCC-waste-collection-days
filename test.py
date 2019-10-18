import csv
import tkinter

# importing csv information, 'r' denotes the reading of the file
with open('/Users/madurasenadeera/github/BCC_waste_collection_days/data/Waste Collection Days.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # print(csv_reader) # prints object for the imported csv file
    # next(csv_reader)  # steps over initial value ("suburb")

    # for line in csv_reader:
    #    print(line[8])

    # unitQn = input('')
    
    number = input('Enter house number \n')
    street = input('Enter street name \n')
    suburb = input('Enter suburb name \n')
    

    for line in csv_reader:
        if ((line[3] == number) and (line[5] == street.upper()) and (line[8] == suburb.upper())):  # line[8]:
            print(line[1], line[3], line[5], line[6], line[8])
        else:
            #print("Invalid suburb name.")
            pass
