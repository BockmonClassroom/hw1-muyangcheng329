# Muyang Cheng
# January 17, 2025

# Importing library
import csv

# define the path
file_path = "/Users/muyangcheng329/Desktop/Doc/Univ/SPR 2025/DS5110/hw1-muyangcheng329/data/Iris.csv"

# open the CSV file
with open(file_path, mode='r') as file:

    # read the file
    csv_reader = csv.reader(file)

    # line count
    line_count = 0

     # print every line 
    for line in csv_reader:
        print(line)
        line_count += 1

    # print the total number of lines
    print(f"Total lines printed: {line_count}")