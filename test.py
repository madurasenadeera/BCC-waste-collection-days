import csv
import tkinter

suburb = input('Enter suburb name: \n')

print(suburb)
# importing csv information, 'r' denotes the reading of the file
# with open('/Users/madurasenadeera/github/BCC_waste_collection_days/data/Waste Collection Days.csv', 'r') as csv_file:
#    csv_reader = csv.reader(csv_file)

# print(csv_reader)
# next(csv_reader)  # steps over initial value ("suburb")

# for line in csv_reader:
#    print(line[8])

# suburb = input('Enter suburb name \n')

# for line in csv_reader:
#    if line[8] == "FOREST LAKE":  # line[8]:
#        print(line)
#    else:
#        print("Invalid suburb name.")
