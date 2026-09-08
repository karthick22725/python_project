import sqlite3

connection = sqlite3.connect("student.db")

connection.execute("create table if not exists student1(id integer primary key,name varchar,age number,dept varchar)")

def add_student():
    name = input("enter the name:")
    age  = input("enter the age:")
    dept = input("enter the department:")
    cursor = connection.execute('insert into student1(name,age,dept) values(?,?,?)',(name,age,dept))
    if cursor:
        print("student added sucessfully...")
    else:
        print("there is an error...coding issue..")

def view_student():
    for row in connection.execute("select * from student1 ORDER BY age asc limit 1"):
        print('{:>5} {:>15} {:>5} {:>20}'.format(row[0],row[1],row[2],row[3]))

def delete_student():
    delete_name=input("enter the name to delete:")
    cursor=connection.execute('delete from student1 where name = ?',(delete_name,))
    if cursor.rowcount > 0:
        print("name deleted successfully...")
    else:
        print("error in deleting...maybe your name not exist in the list")

def search_student():
    search_name=input("enter the search name:")
    a = connection.execute("select * from student1 where name = ?",(search_name,))
    row=a.fetchall()
    if row:
        print(row)
    else:
        print("not exist...")
        
def update_student():
    update_name=input("enter the name for updation:")
    a = connection.execute("select * from student1 where name = ?",(update_name,))
    if a.fetchone():
        c=1
        while c==1:
            a = connection.execute("select * from student1 where name = ?",(update_name,))
            print(a.fetchone())
            print("(1)change name (2)change age (3)change dept (4)save")
            choice=int(input("enter the choice:"))
            match choice:
                case 1:
                    new_name =input("enter the name:")
                    connection.execute("update student1 set name =? where name =?",(new_name, update_name))
                    update_name = new_name
                case 2:
                    new_age =input("enter the age:")
                    connection.execute("update student1 set age =? where name =?",(new_age, update_name))
                case 3:
                    new_dept= input("enter the dept:")
                    connection.execute("update student1 set dept =? where name =?",(new_dept, update_name))
                case 4:
                    c=0
                    print("saved successfully")
                case _:
                    print("default")
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
    choice=int(input("Enter the choice:"))
    match choice:
        case 1:
            add_student()
        case 2:
            view_student()
        case 3:
            delete_student()
        case 4:
            search_student()
        case 5:
            update_student()
        case 6:
            break
        case _:
            print('invalid choice...')

connection.commit()
connection.close()