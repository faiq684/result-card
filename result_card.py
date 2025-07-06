student_names = ['faiq', 'ali', 'zain', 'khabeer']
ages = (20, 20, 20, 20)
grade = (10, 10, 10, 10)
roll_numbers = (1111, 2222, 3333, 4444)
subjects = ['English', 'Math', 'Computer', 'Urdu']
marks = [
    (45, 50, 45, 44),
    (50, 45, 40, 50),
    (40, 40, 50, 30),
    (45, 40, 50, 50)
]

input_rollNumber = int(input("Enter Your Roll Number: "))

if input_rollNumber in roll_numbers:
    index = roll_numbers.index(input_rollNumber)

    total = sum(marks[index])
    percentage = total / len(subjects)

    print('\n===== Result Card =====')
    print('Name       :', student_names[index])
    print('Age        :', ages[index])
    print('Class      :', grade[index])
    print('Subjects   :', subjects)
    print('Marks      :', marks[index])
    print('Total      :', total)
    print('Percentage :', percentage)
else:
    print("Incorrect Roll Number!")
