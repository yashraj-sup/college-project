import os
import mysql.connector
conn=mysql.connector.connect(host="localhost", user="yash", password=os.environ["DB_PASSWORD"], database="College")
cursor=conn.cursor()
print("Database connected successfully!")
while True:
    print("\n--STUDENT MANAGEMENT SYSTEM ---")
    print("1.Add Student")
    print("2.View Students")
    print("3.Update Students")
    print("4.Delete Student")
    print("5.Exit")
    choice=input("Enter your choice:")
    try:
        if choice=='1':
            name=input("Enter Student Name:")
            age=int(input("Enter Age:"))
            marks=int(input("Enter Marks:"))
            query="INSERt INTO Student(name,age,marks)VALUES(%s,%s,%s)"
            values=(name,age,marks)
            cursor.execute(query,values)
            conn.commit()
            print("Student added successfully!")
        elif choice=='2':
            cursor.execute("SELECT *FROM Student")
            records=cursor.fetchall()
            print("\nStudent Records:")
            for row in records:
                print(row)
        elif choice=='3':
            sid=int(input("Enter Student ID:"))
            marks=int(input("Enter Student Marks:"))
            query="UPDATE Student SET marks=%s WHERE id=%s"
            cursor.execute(query,(marks,sid))
            conn.commit()
            if cursor.rowcount>0:
                print("Student updated successfully!")
            else:
                print("Student ID not found!")
        elif choice=='4':
            sid=int(input("Enter Student ID:"))
            query="DELETE FROM Student WHERE ID=%s"
            cursor.execute(query,(sid,))
            conn.commit()
            if cursor.rowcount>0:
                print("Student deleted successfully!")
            else:
                print("Student Id not found!")
        elif choice=='5':
            print("Exiting program..")
            break
        else:
            print("Invalid choice!")
    except(mysql.connector.Error,ValueError) as e:
        conn.rollback()
        print("Error:", e)
cursor.close()
conn.close()
print("Database connection closed!")
