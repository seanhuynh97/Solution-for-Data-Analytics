# -*- coding: utf-8 -*-
"""
Password Check
Purpose: This module allows the login module to check the password entered for requirements
and to create a new password if required.
Password strength:
    Requirements:
        Max 12 characters
        (3 of 4) Upper, Lower, Special Char, Digit
"""
import getpass

def check_password(password):
    #checks if a password meets requirements
    special_char = ['!','@','#','$','%','^','&','*']
    pw_req = 0                
    lower = False
    upper = False
    digit = False
    special = False

    for char in password:
        if char.islower():
            if lower == True:
                continue
            lower = True
            pw_req += 1
        elif char.isupper():
            if upper == True:
                continue
            upper = True
            pw_req += 1
        elif char.isdigit():
            if digit == True:
                continue
            digit = True
            pw_req += 1
        elif char in special_char:
            if special == True:
                continue
            special = True
            pw_req += 1     
        
    if pw_req >= 3:
        return True
    else:
        return False

def enter_password():
    #Allows a user to enter a password
    pw_strength = False
    match = False

    while match == False:                      
        password = getpass.getpass("Enter a Password: ").strip()
        
        if len(password) > 12:
            print("Password must not exceed 12 characters")
            continue
        
        pw_strength = check_password(password)
        
        if pw_strength == False:
            print("Password Strength: Weak")
            print("Requirements (3 of 4): 1 Upper, 1 Lower, 1 Number, 1 Special Char (!@#$%^&*)")
            continue
                                                                                          
        if password != getpass.getpass("Verify Password: ").strip():
            print("Password does not match! Please enter a new Password.")
            match = False
        else:
            match = True

    return password        

### Testing
#saved_pw = enter_password()   
#print("Thank you for entering a valid password")  
#print("Saved Password: " + saved_pw)                                                       
