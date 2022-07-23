#short script for pinging multiple ip address from csv file and saving the report in txt file.
import csv
import os

with open('apex-ip-singapore.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    file = open('apex-ip-result.txt', 'a')
    for row in reader_obj:
        print(row[0])
        result = os.popen(f"ping {str(row[0])} -c 1 | grep 'avg'").read()
        print(result)
        file.write(row[0])
        file.write(f"\n")
        file.write(result)
        file.write(f"\n")
        file.write(f"------------------------------------------------------------")
        file.write(f"\n")
    file.close()
