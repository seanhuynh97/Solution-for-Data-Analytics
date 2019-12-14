# -*- coding: utf-8 -*-
"""
New_Employee
Purpose: To add a new employee to the employee database.

"""
import sqlite3
import Password_Check
from email_validator import validate_email, EmailNotValidError

def add_employee():
    # First Name
    first_name = input("Please enter your first name: ").strip().title()
    while not first_name:
        first_name = input("Please enter your first name: ").strip().title()

    # Last Name
    last_name = input("Please enter your last name: ").strip().title()
    while not last_name:
        last_name = input("Please enter your last name: ").strip().title()

    # Email
    used = True
    while used:
        is_valid = False
        while is_valid == False:
            email = input("Please enter your email: ").lower()            
            while not email:
                email = input("Please enter your email: ").lower()
            try:    
                valid = validate_email(email)
                email = valid["email"]
                is_valid = True
            except:
                print("'" + email + "' is not valid. Please enter another email.")
                is_valid = False

        with sqlite3.connect('OS_Employee.db') as db:
            cursor = db.cursor()
        find_email = 'SELECT * FROM Employee where Email = ?'
        cursor.execute(find_email, [email])

        if cursor.fetchall():
            used = True
            print("That email is already in use. Please enter a new email: ")
        else:
            used = False

    # Password
    password = Password_Check.enter_password()

    # Confirmation
    print("\nThe following user information was entered:")
    print("Name: " + first_name + " " + last_name)
    print("Email: " + email)
    confirm = input("\nPlease confirm to complete registration. [Y/N] ")
    if confirm.lower() == "n":
        print("\nRegistration has been cancelled.")
        return

    # ID - Get max employeeID in database and add 1
    with sqlite3.connect('OS_Employee.db') as db:
        cursor = db.cursor()
    cursor.execute("SELECT max(EmployeeID) FROM employee")
    max_id = cursor.fetchone()
    new_id = int(max_id[0]) + 1

    # Add to Database
    insert_data = ''' INSERT INTO Employee (EmployeeID, FirstName, LastName, Email, Password) VALUES(?,?,?,?,?)'''
    with sqlite3.connect('OS_Employee.db') as db:
        cursor = db.cursor()
    cursor.execute(insert_data, [new_id, first_name, last_name, email, password])
    db.commit()
    print("\n" + first_name + " " + last_name + " has been registered.")


'''TESTING'''
# Uncomment for testing of New_Employee without running Main.py#
#add_employee()
