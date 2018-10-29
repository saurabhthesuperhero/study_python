import csv
import pprint

# csv -> list
a_list = []
f = open('filename.csv', 'r')
reader = csv.reader(f)
for row in reader:
    a_list.append(row)
f.close()

with open('filename.csv', 'r') as f:
    reader = csv.reader(f)
    a_list = list(reader)

pprint.pprint(a_list)

# list -> csv
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
    writer.writerow(['hello, world', 'eggs', 'bacon', 'ham'])
    writer.writerow([1, 2, 3, 4])


with open('filename.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

