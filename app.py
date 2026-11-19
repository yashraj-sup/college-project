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
if __name__ == "__main__":
    app.run(debug=True)
