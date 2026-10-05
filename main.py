# list of three students named Jon, Kim and Lee
# function to print 'Hi name' for each student in the list
# call the function

import csv
names = ['jon', 'Kim', 'Lee']


def greet_all(name_list):
    for name in name_list:
        print(f'Hi {name}')


names.append('David')
print('Total count:', len(names))

greet_all(names)
print()

scores = [3.2, 2.8, 3.9]

avg_score = sum(scores) / len(scores)
print()

for i in range(len(scores)):
    if scores[i] > avg_score:
        print(f'Above average score: {scores[i]}')

students = {
    "John": {"gpa": 3.5, "major": "math"},
    "Kim": {"gpa": 2.8, "major": "Bio"},
}

print(students["John"]["gpa"])
print()


with open("students.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
