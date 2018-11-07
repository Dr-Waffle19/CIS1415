#These three blocks initialize student dictionaries with lists of their
#various scores stored as the values.
lloyd = {
    'name': 'Lloyd',
    'homework': [90.0, 97.0, 75.0, 92.0],
    'quizzes': [88.0, 40.0, 94.0],
    'tests': [75.0, 90.0]
}
alice = {
    'name': 'Alice',
    'homework': [100.0, 92.0, 98.0, 100.0],
    'quizzes': [82.0, 83.0, 91.0],
    'tests': [89.0, 97.0]
}
tyler = {
    'name': 'Tyler',
    'homework': [0.0, 87.0, 75.0, 22.0],
    'quizzes': [0.0, 75.0, 78.0],
    'tests': [100.0, 100.0]
}

#Initializes a list to be iterated through in a for list to calculate and print
#various statistics pertaining to their scores and grades.
students = [lloyd,alice,tyler]

#This for loop iterates through the earlier initialized list and prints out the
#name of the student, scores, average scores, and overall percentage of that student.
for student in students:
    print(student['name'])
    print('Homework scores:', student['homework'])
    print('Homework average score:', (sum(student['homework']) / 4))
    print('Quizzes scores:', student['quizzes'])
    print('Quizzes average score:', (sum(student['quizzes']) / 3))
    print('Tests scores:', student['tests'])
    print('Tests average score:', (sum(student['tests']) / 2))
    print('Student percentage: %.2f%%' % ((sum(student['homework']) +
          sum(student['quizzes']) + sum(student['tests'])) / 9.0))
    print()

