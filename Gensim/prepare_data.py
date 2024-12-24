import csv , json

with open('data/Friends.csv','r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

with open('data/Friends.json','w') as file:
    json.dump(data , file ,  indent = 4)