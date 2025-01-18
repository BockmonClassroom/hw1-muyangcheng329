# Muyang Cheng
# January 17, 2025

# Importing library
import csv

# define the path
file_path = "/Users/muyangcheng329/Desktop/Doc/Univ/SPR 2025/DS5110/test/hw1-muyangcheng329/data/Iris.csv"

# open the CSV file
with open(file_path, mode='r') as file:

    # read the file
    csv_reader = csv.reader(file)

    # print every line 
    for line in csv_reader:
        print(line)