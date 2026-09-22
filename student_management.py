import sqlite3

connection = sqlite3.connect("studentdata.db")

connection.execute("create table if not exists student1(id integer primary key,name varchar,age number,dept varchar, email varchar, phone varchar)")

def add_student():
    name = input("enter the Name:").strip()
    age  = input("enter the Age:")
    dept = input("enter the Department:")
    email = input("enter the Email:")
    phone  = input("enter the Phone Number:")
    if len(phone) == 10 and phone.isdigit():
        if '@' in email and '.' in email:
            cursor = connection.execute('insert into student1(name,age,dept,email,phone) values(?,?,?,?,?)',(name,age,dept,email,phone))
            print("student added successfully..")
            connection.commit()
        else:
            print("gmail not correct")
    else:
        print("number not in correct format")

def view_student():
    found = False
    for row in connection.execute("select * from student1"):
        print('{:>5} {:>15} {:>5} {:>7} {:>20} {:>14}'.format(row[0],row[1],row[2],row[3],row[4],row[5]))
        found = True
    if not found:
        print("no data found..")
    

def delete_student():
    delete_name=input("enter the name to delete:").strip()
    a = connection.execute("select * from student1 where name = ?",(delete_name ,))
    row =a.fetchall()
    if row:
        if len(row)>= 2:
            while True:
                for student in row:
                            print(
                                "ID:", student[0],
                                "| Name:", student[1],
                                "| Age:", student[2],
                                "| Department:", student[3],
                                "| Email:", student[4],
                                "| Phone:", student[5]
                            )
                id = input("enter the id to delete:")
                check =connection.execute("select * from student1 where id=? and name=?",(id,delete_name))
                if check.fetchone():
                    break
                else:
                    print("wrong id..")
                
        else:
            id = row[0][0]
        delete = connection.execute("delete from student1 where id=?",(id ,))
        print("deleted successfully..")
        connection.commit()
    else:
        print("not exist..")

def search_student():
    search_name=input("enter the search name:").strip()
    a = connection.execute("select * from student1 where name = ?",(search_name,))
    row=a.fetchall()
    if row:
        for student in row:
            print('{:>5} {:>15} {:>5} {:>7} {:>20} {:>14}'.format(student[0],student[1],student[2],student[3],student[4],student[5]))
    else:
        print("not exist...")
        
def update_student():
    update_name=input("enter the name for updation:").strip()
    a = connection.execute("select * from student1 where name = ?",(update_name,))
    row = a.fetchall()
    if row:
        for student in row:
            print(
                "ID:", student[0],
                "| Name:", student[1],
                "| Age:", student[2],
                "| Department:", student[3],
                "| Email:", student[4],
                "| Phone:", student[5]
            )
        if (len(row) >= 2):
            while True:
                id=input("enter the id you wanna update:")

                check = connection.execute("select * from student1 where id = ? and name = ?",(id, update_name))

                if check.fetchone():
                    break
                else:
                    print("wrong id....")

        else:
            id= row[0][0]
        c=1
        while c==1:
            
            print("(1)change name (2)change age (3)change department (4)change email (5)change number (6)save")
            choice=input("enter the choice:")
            match choice:
                case '1':
                    new_name =input("enter the name:").strip()
                    connection.execute("update student1 set name =? where id =?",(new_name, id))
                case '2':
                    new_age =input("enter the age:")
                    connection.execute("update student1 set age =? where id =?",(new_age, id))
                case '3':
                    new_dept= input("enter the department:")
                    connection.execute("update student1 set dept =? where id =?",(new_dept, id))
                case '4':
                    new_email= input("enter the email:")
                    if '@' in new_email and '.' in new_email:
                        connection.execute("update student1 set email =? where id =?",(new_email, id))   
                    else:
                        print("wrong format...")
                case '5':
                    new_phone=input("enter the number:")
                    if len(new_phone) == 10 and new_phone.isdigit():
                        connection.execute("update student1 set phone =? where id =?",(new_phone, id))
                    else:
                        print("wrong number format..")
                case '6':
                    c=0
                    connection.commit()
                    print("saved successfully")
                case _:
                    print("invalid choice..")
            a= connection.execute("select * from student1 where id = ?",(id,))
            print(a.fetchone())
    else:
        print("student not exist...")

while True:
    print("=" * 30)
    print("student management")
    print("=" * 30)
    print("(1) add the student")
    print("(2) view the students")
    print("(3) delete the student")
    print("(4) search the student")
    print("(5) update the student")
    print("(6) exit")
    print("=" * 30)
    choice=input("Enter the choice:")
    match choice:
        case '1':
            add_student()
        case '2':
            view_student()
        case '3':
            delete_student()
        case '4':
            search_student()
        case '5':
            update_student()
        case '6':
            break
        case _:
            print('invalid choice...')

connection.commit()
connection.close()