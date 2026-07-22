def save_student():
            with open("student.txt", "w") as file:
                  for student in students:
                        file.write(student["name"] +  "|" + str(student["age"]) + "|" + student["dept"]+ "\n")


def add_function():
            name=str(input("ENTER THE NAME        : "))
            age=int(input("ENTER THE AGE         : "))
            dept=str(input("ENTER THE DEPARTMENT  : "))

            student={
                  'name' : name,
                  'age' : age,
                  'dept' : dept
                }
            students.append(student)
            print(f"student named {name} register sucessfully..")
            save_student()

def view_function():
            if len(students)>0:
                print("========== STUDENTS ==========")
                for student in students:
                        print("NAME       :", student['name'])
                        print("AGE        :", student['age'])
                        print("DEPARTMENT :", student['dept'])
                        print("--------------------------------")
                print(" END OF LIST....")
            else:
                  print("no students avaliable....")

def search_function():
            search_name=input("\tENTER THE STUDENT NAME: ")
            for student in students:
                    if student['name'] == search_name:
                        print(f"NAME       : {student['name']}")
                        print(f"AGE        : {student['age']}")
                        print(f"DEPARTMENT : {student['dept']}")

def delete_function():
            i=0
            status = "not found"
            delete_name=input("ENTER THE STUDENT NAME: ")
            for student in students:
                
                    if student['name'] == delete_name:
                        print(f"NAME       : {student['name']}")
                        print(f"AGE        : {student['age']}")
                        print(f"DEPARTMENT : {student['dept']}")
                        option=input("are you sure to delete? (yes/no)")
                        status = 'found'
                        if option == 'yes':
                              students.pop(i)
                              print(f"deletion successfully...( {student['name']})")
                              i=i-1
                        else:
                               print("canceling the deletion....")
                    i=i+1
            if status=="not found":
                print("the name you looking for not found in the list...")
            save_student()

'''========== STUDENT MANAGEMENT ==========
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit,,..'''

students=[]
with open("student.txt", "r") as file:
      for line in file:
            data= line.split('|')
            student={
                  'name' : data[0],
                  'age' : int(data[1]),
                  'dept' : data[2].strip()
            }
            students.append(student)

while (True):
    print("\t========== STUDENT MANAGEMENT ==========")
    print("\t(1) ADD STUDENT INFORMATION")
    print("\t(2) VIEW STUDENT INFORMATION")
    print("\t(3) SEARCH STUDENT INFORMATION")
    print("\t(4) DELETE STUDENT INFORMATION")
    print("\t(5) EXIT")
    print("\t\t*****************")
    choice=int(input("\t ENTER THE OPTION: "))
    match (choice):
        case 1:
            add_function()
        case 2:
            view_function()
        case 3:
            search_function() 
        case 4:
            delete_function()
        case 5:
            print("end of program...")
            break
        case _:
            print("invalid choice")
    

     

     