import csv

with open("student_db.csv","rb") as f:
    reader = csv.reader(f)
    mylist = list(reader)

#print mylist

data = dict()

for temp_list in mylist:
    data[temp_list[0]] = temp_list[1]

def get_student(index):
    return data.get(index)

