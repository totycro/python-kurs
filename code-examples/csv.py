import csv

f = open("woods.csv")
reader = csv.DictReader(f)


print("dict reader")
for entry in reader:
    print(entry)


f = open("woods.csv")
reader = csv.reader(f)

print("regular reader")
for entry in reader:
    print(entry)
