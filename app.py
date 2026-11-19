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
if __name__ == "__main__":
    app.run(debug=True)
