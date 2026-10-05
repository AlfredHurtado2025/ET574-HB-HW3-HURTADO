# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]

# function to print 'Hi name' for each student in the list
def greet_all(name_list):
    for name in name_list:
        print(f"Hi {name}")

# append David to the names list
students.append("David")

# print the total number of names
print("Total count:", len(students))

# call the function
greet_all(students)

# print an empty line
print()

# list of scores
scores = [3.2, 2.8, 3.9]

# calculate the average score
avg_score = sum(scores) / len(scores)

# print the average score
print(f"Average score: {avg_score:.2f}")

# print scores above the average
for i in range(len(scores)):
    if scores[i] > avg_score:
        print(f"Above average score: {scores[i]}")

# print an empty line
print()

# dictionary of students with GPA and major
students = {
    "John": {"gpa": 3.5, "major": "math"},
    "Kim": {"gpa": 2.8, "major": "Bio"}
}

# print John's GPA
print(students["John"]["gpa"])

# print an empty line
print()

import csv

with open("students.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


