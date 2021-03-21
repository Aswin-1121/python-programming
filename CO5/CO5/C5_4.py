import csv
with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "player", "team"])
    writer.writerow([1, "bramman", "TVM strikers"])
    writer.writerow([2, "nithin", "kollam fives"])



with open('protagonist.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1]+" "+row[2])
