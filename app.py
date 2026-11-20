import os
import mysql.connector
from flask import Flask, render_template, request, redirect
app=Flask(__name__)
def helper_function():
    return mysql.connector.connect(host="127.0.0.1",user="yash",password=os.environ["DB_PASSWORD"],database="College")
@app.route("/")
def index():
    conn=helper_function()
    cursor=conn.cursor()
    #execute queries
    cursor.execute("SELECT *FROM Student")
    result=cursor.fetchall()
    #first close cursor and then connection(always)
    cursor.close()
    conn.close()
    return render_template("index.html", students=result) #first argument is the file name inside templates/ and after it everyhting is a varibale,students=result gets fetched rows to the loop under the name students
@app.route("/add", methods=["POST"])
def add_student():
    try:
        name=request.form["student_name"]
        age=int(request.form["student_age"])
        marks=int(request.form["student_marks"])
    except ValueError:
        return "Invalid value"
    conn=helper_function()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO Student (Name, Age, Marks) VALUES(%s, %s, %s)", (name, age, marks))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")
@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    conn=helper_function()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM Student WHERE ID=%s",(student_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")
@app.route("/edit/<int:student_id>")
def edit_student(student_id):
    conn=helper_function()
    cursor=conn.cursor()
    cursor.execute("SELECT *FROM Student WHERE ID=%s",(student_id,))
    row=cursor.fetchone() #fetchone() reurns the next single row of a query result as a tuple, returns None when no more rows are available
    cursor.close()
    conn.close()
    if row is None:
        return "Student not found"
    return render_template("edit.html", student=row)
@app.route("/update/<int:student_id>", methods=["POST"])
def update_student(student_id):
    try:
            name=request.form["student_name"]
            age=int(request.form["student_age"])
            marks=int(request.form["student_marks"])
    except ValueError:
            return "Invalid value"
    conn=helper_function()
    cursor=conn.cursor()
    cursor.execute("UPDATE Student SET Name=%s, Age=%s, Marks=%s WHERE ID=%s",(name, age, marks, student_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)
