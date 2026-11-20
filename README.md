# A Student Management System with add,update,edit,delete feature built with Flask and MySQL
## Requirements
 A MYSQL server with a user called yash and database called College
## Setup
 1. Run ` 
 college.sql
 `
 in Workbench to create the database and table

 2. Create a venv with `
python3 -m venv venv
`
3. Activate it with
 `
source venv/bin/activate
`
4. Install dependencies with 
` 
  pip install -r requirements.txt
`
5. Set the password with 
`
export DB_PASSWORD='...'
`
## Run 
`
python app.py
`
- open http://127.0.0.1:5000
