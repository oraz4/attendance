import os

os.startfile('c:\Program Files\RF Enabled\PlaceCard\PlaceCard.exe')

who = int(input('You want to add a STUDENT or an INSTRUCTOR?\nPlease choose: 1. STUDENT  2.INSTRUCTOR\n'))
while who not in range(1,3):
    print('Please enter only 1 or 2\n')
    who = int(input('You want to add a STUDENT or an INSTRUCTOR?\nPlease choose: 1. STUDENT  2.INSTRUCTOR\n'))
if who == 1:
    cohort = int(input('Please enter 1 or 2 to take attendance:\n1. Cohort 1\n2. Cohort 2\n'))
    while cohort not in range(1,3):
        print('Not an appropriate choice. Try again...')
        cohort = int(input('Please enter 1 or 2 to take attendance:\n1. Cohort 1\n2. Cohort 2\n'))

    if cohort == 1:
        student_name = input("Please enter student's name: ")
        student_id = input("Put the " + student_name + "'s ID: ")
        with open('cohort1.txt', 'a') as doc:
            doc.write('\n')
            doc.write(student_id + ', ' + student_name)
        doc.close()
    if cohort == 2:
        student_name = input("Please enter student's name: ")
        student_id = input("Put the " + student_name + "'s ID: ")
        with open('cohort2.txt', 'a') as doc:
            doc.write('\n')
            doc.write(student_id + ', ' + student_name)
        doc.close()
elif who == 2:
    instructor_name = input("Please enter instructors's name: ")
    instructor_id = input("Put the " + instructor_name + "'s ID: ")
    with open('teacher.txt', 'a') as doc:
        doc.write('\n')
        doc.write(instructor_id+', '+instructor_name)
    doc.close()

os.system('TASKKILL /F /IM PlaceCard.exe')
