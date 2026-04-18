import json
import csv


def json_to_csv(json_file, csv_file):
   
    with open(json_file, 'r') as jf:
        data = json.load(jf)

    headers = data[0].keys()

    
    with open(csv_file, 'w', newline='') as cf:
        writer = csv.DictWriter(cf, fieldnames=headers)
        
        writer.writeheader()   
        writer.writerows(data) 

    print("Conversion completed successfully!")


json_to_csv('fileconversion.json', 'converted.csv')