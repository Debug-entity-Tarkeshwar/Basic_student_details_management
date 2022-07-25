admins = {'python':'pass123@','Tarkeshwar':'pass@123'}
studentDict = {'Rakesh':[195119,85] ,
               'aditya':[195107,90],
               'kartik':[193059,87]}
def addnewstudent():
    name = input('enter name of new student:')
    rollno_and_marks = input('enter rollno. and marks of ' + name +':')
    studentDict[name] = rollno_and_marks
    print('successfully added student details....')
def deletestudent():
    name = input('enter name of student you want to delete:')
    if name in studentDict:
        del studentDict[name]
        print('successfully deleted student details....')
    else:
        print("there is no student with such name!")
def editstudentdetail():
    name = input('enter name of student you want to edit:')
    if name in studentDict:
        rollno_and_marks = input('enter rollno. and marks of ' + name +':')
        studentDict[name] = rollno_and_marks
        print('successfully updated student details....')
    else:
        print("there is no student with such name!")
def viewstudentlist():
    print(studentDict)
def main():
    print('''
    Welcome to Student Marks Management.
     
     [1] Add new student.
     [2] Delete existing student.
     [3] Edit existing student details.
     [4] View student list
     [5] Exit
     ''')
    action = input("what would you like to do? choose anyone from 1-4:")
    if action == '1':
     addnewstudent()
    elif action == '2':
     deletestudent()
    elif action == '3':
     editstudentdetail()
    elif action == '4':
      viewstudentlist()  
    elif action == '5':
     exit()
    else:
        print("enter a valid choice try again!")
login = input("Username:")
password = input("password:")
if login in admins:
    if admins[login] == password:
        print(' Welcome',login)
        main()
        while True:
            choice = input('would you like to continue y/n:')
            if (choice == 'y'):
              main()
            else:
              exit()
    else:
        print('Invalid password!, will detonate in 5 seconds...')
else:
    print('invalid username!')
    
