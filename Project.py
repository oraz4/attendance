import os
import time


os.startfile('c:\Program Files\RF Enabled\PlaceCard\PlaceCard.exe')

subject = input('Write your subject name: ')
subject= subject.lower()

# find out in which cohort to take attendance and which data to import
# make a dictionary from a file of names and ID

cohort = int(input('Please enter 1 or 2 to take attendance:\n1. Cohort 1\n2. Cohort 2\n'))

while True:
    if cohort not in range(1,3):
        print('Not an appropriate choice. Try again...')
        cohort = int(input('Please enter 1 or 2 to take attendance:\n1. Cohort 1\n2. Cohort 2\n'))
    else:
        break
print('Now we will take attendace for Cohort ' + str(cohort))

if cohort == 1:
        with open('Cohort1.txt', 'r') as document:
            student_dict = {}
            for line in document:
                line = line.rstrip("\n")
                line1 = line.split(',')
                if not line1:
                    continue
                student_dict[int(line1[0])] = line1[1]
elif cohort == 2:
    with open('Cohort2.txt', 'r') as document:
        student_dict = {}
        for line in document:
            line = line.rstrip("\n")
            line1 = line.split(',')
            if not line1:
                continue
            student_dict[int(line1[0])] = line1[1]

with open('teacher.txt', 'r') as document:
    teacher_dict = {}
    for line in document:
        line = line.rstrip("\n")
        line1 = line.split(',')
        if not line1:
            continue
        teacher_dict[int(line1[0])] = line1[1]

name = time.strftime("%d%m %I%M%p")
list1 = []
# Open file with name 'Data' and add time on the top of it
with open('C:/Users/giyoe/Desktop/Python/Project/Attendance/Cohort ' + str(cohort) +'/' + subject + '/Attendance' + str(name) + '.csv', 'a') as student:
    min1 = time.strftime("%M")
    student.write(time.strftime("Attendance list at %H:%M %d %B %Y"))
    student.write('\n')
    student.write('\n')
    while True:
        x = input()
        x = int(x)
        if x in teacher_dict:
            break
        # if student is within 15 minutes
        elif float(time.strftime("%M"))-float(min1) < 1:
            if x not in list1:
                if x in student_dict:
                    student.write(student_dict[x])
                else:
                    student.write(str(x))
                student.write(',')
                student.write(time.strftime("Present \n"))
        # if student is after 15 minutes the class started it marks him late
        elif float(time.strftime("%M"))-float(min1) >= 1:
            if x not in list1:
                if x in student_dict:
                    student.write(student_dict[x])
                else:
                    student.write(str(x))
                student.write(',')
                student.write(time.strftime("Present"))
                student.write(',')
                late = float(time.strftime("%M"))-(float(min1))
                student.write('Late for ')
                student.write(str(int(late)))
                student.write(' minutes')
                student.write('\n')
        if x not in list1:
            list1.append(x)

    student_copy = student_dict.copy()   # create a copy of our original data/dictionary

    index = len(list1) - 1
    while index >= 0:
        if list1[index] in student_copy:
            del student_copy[list1[index]]
        index -= 1

    for i in student_copy.values():
        student.write(i)
        student.write(',')
        student.write('Absent')
        student.write('\n')
    student.write('\n')

# close/save the document and close PlaceCard.exe
student.close()
os.system('TASKKILL /F /IM PlaceCard.exe')
