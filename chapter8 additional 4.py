Student_grade = {
    'Jimoh Olu': {
        'test_labwork_homeworks': [87, 91, 68],
        'Midterm': 80,
        'Final': 91
    },
    'Taju Kulu': {
        'test_labwork_homeworks': [99, 78.25],
        'Midterm': 87,
        'Final': 75
    },
    'Bunmi Ojo': {
        'test_labwork_homeworks': [98.75, 80],
        'Midterm': 40,
        'Final': 75
    },
}

user_input = input('Enter student full name: ')

while user_input != 'exit':
    if user_input in Student_grade:
# Get values from the inputed nested dictionary 
        test_labwork_homeworks = Student_grade[user_input]['test_labwork_homeworks']
        midterm = Student_grade[user_input]['Midterm']
        final = Student_grade[user_input]['Final']

# print information about student grade
        for hw, score in enumerate(test_labwork_homeworks):
            print('Homework %d: %d' % (hw, score))

        print('Midterm: %s' % midterm)
        print('Final: %s' % final)

# student total grade
        total_points = sum([i for i in test_labwork_homeworks]) + midterm + final
        print('Final percentage: %f%%' % (100*(total_points / 500.0)))

    user_input = input('Enter student full name: ')
