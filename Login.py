# -*- coding: utf-8 -*-
"""
Login
Purpose: Login used for the group project. Will be called from Main. Connects 
to an employee database and verifies user email/password before allowing a 
successful login.
"""
import getpass
import sqlite3
import Password_Check
import Email_Send

def verify_login(user,pw):
    #Verify User/Password exist in employee db
    conn = sqlite3.connect('OS_Employee.db')
    
    with conn:
        cur = conn.cursor()
                
        try:
            #Query database for User and Password
            cur.execute("SELECT COUNT (*) FROM Employee WHERE(Email = '" + 
                        user +"' AND Password = '" + pw + "')")
            #Get results
            results = cur.fetchone()
        
            #Should only have one record in the array            
            if results[0]==1:
                return True
            else:
                return False
            
        except:
            print("Database Connection Failed")
            return False

def update_password(user, pw):
    #Update employee DB with new password
    conn = sqlite3.connect('OS_Employee.db')
    
    with conn:
        cur = conn.cursor()
                
        try:
            #Query database for User and Password
            cur.execute("UPDATE Employee SET Password = '" + pw + "' WHERE Email = '" + 
                        user + "'")
            #Save Results
            conn.commit()
            return True 
        except:
            print("Failed to Update Password.\n")
            return False

def forgot_password(user):
    #User Reset Password
    password = ""
    conn = sqlite3.connect('OS_Employee.db')
    
    with conn:
        cur = conn.cursor()
                
        try:
            #Query database for User and Password
            cur.execute("SELECT COUNT (*) FROM Employee WHERE Email = '" + 
                        user + "'")
            #Get results
            results = cur.fetchone()
        
            #Should only have one record in the array            
            if results[0]==1:
                password = Email_Send.forgot_password(user)
                print("Please login using the temporary password.")
            else:
                print("\nUser does not exist in database!")
        except:
            print("\nFailed to Update Password. Please try again.")       
    
    return password
    
def verify_password(user, pw):
    #Check if password meets requirements
    pw_strength = Password_Check.check_password(pw)

    if pw_strength == True:
        return
    else:
        #Password does not meet requirements. Prompt to update
        print("Your password does not meet password requirements." +
              "\nPlease update your password.")
        pw = Password_Check.enter_password()
        success = update_password(user, pw)
        
        if success == True:
            print("Password has been updated!")
            
def login():
    print("\nWelcome to Office Solutions Data Analytics!" +
          "\n\nPlease login to begin.\n" +
          "\n\tLogin Help:" +
          '\n\t   Enter "forgot" into the password field to reset password.' +
          '\n\t   Enter "exit" into email field to exit program without logging in.')

    connected = False
    
    #Loop Login Request until a successful login
    while connected == False:
        user = input("Email: ").lower().strip()   
        
        if user == "exit":
            return
        elif user == "forgot":
            print("Please enter a valid email to reset password.")
            continue
        
        password = getpass.getpass("Password: ").strip()
    
        if password == "forgot":
            #check if a valid email
            if user != "":
                password = forgot_password(user)
                if password != "":
                    update_password(user, password)
                    continue
                else:
                    print("Please enter a valid email to reset password.")
                    continue
            else:
                print("Please enter a valid email to reset password.")
                continue
        elif password == "exit":
            return
                    
        connected = verify_login(user, password)

        if connected == True:
            print("\nLogin Successful!\n")
            
            #Check if password meets current requirements
            verify_password(user, password)
            
            return True
        else:
            print("\nLogin Failed!\n\n" + "Please verify email and password and retry.")


'''Testing'''
#login()        
