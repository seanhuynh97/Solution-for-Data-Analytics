# -*- coding: utf-8 -*-
"""
Password Reset Email
Purpose: This module is called from the login file and allows a user to reset their 
password if it is forgotten or they are locked out of the account.        
"""

import smtplib, ssl
import random

def forgot_password(email):
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    receiver_email = email
    sender_email = "PythonCharmers110A@gmail.com"
    sender_password ="sjsu110A"
    defaultPass = "sjsu"
    
    #Create Random number to append to default password
    for i in range(6):
        defaultPass += str(random.randint(0,9))
        i+=1
    
    #Create string containing the new login information
    account_info = "\n\t\tUser: " + receiver_email + "\n\t\tPassword: " + defaultPass 
    
    #Create Subject and Body of email    
    subject = "Password Reset"
    body = """\
    
    The Password has been reset for the Office Solutions account associated with this email.
    Please login with the following temporary password and follow prompts to reset your password:\n"""
    
    ps = "\n\n\n\nThe information in this email is being used solely for a college coding project.\nIf you have receievd this email in error, please disregard."
    
    #Compose the email message
    message = 'Subject: {}\n\n{}'.format(subject, body)
    
    #append login information to email message
    message += account_info           
    message += ps
    
    #Send email using pythoncharmers account
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
    
    print("\nA temporary password has been sent to: " + receiver_email)  

    #Return password so it can be updated in database
    return defaultPass    
