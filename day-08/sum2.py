import csv
with open("advertising.csv","r") as csv_file:
    csv_reader=csv.reader(csv_file)
    with open("new_advertising.csv","w",newline="") as new_file:
        csv_writer=csv.writer(new_file)
        for line in csv_reader:
            csv_writer.writerow(line)