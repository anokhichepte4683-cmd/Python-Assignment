import csv
def count_rows(file_name):
    with open(file_name,'r') as file:
        csv_reader =csv.reader(file)
        row_count = sum(1 for row in csv_reader)
    return row_count

file_name = "patil.csv"
rows = count_rows(file_name)
print("Total number of row is ",rows )