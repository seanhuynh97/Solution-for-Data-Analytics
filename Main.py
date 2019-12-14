# -*- coding: utf-8 -*-
"""
Main
Purpose: Main file for the project that includes a menu for navigating to the
         different sections (files) of the program.
"""
import Login
import New_Employee
import Profits_Top
import Profits_Bottom
import Regions
import Category
import Top_Customers
import States


def pause():
    #Call Input to pause screen
    input("Press 'Enter' to continue...")

def mainmenu():
    program_run = True

    #Display Menu
    while program_run == True:
        print("\nOffice Solutions Data Analytics" +
              "\nPlease make a selection from the menu below:")
        print("\n\tMain Menu:" +
              "\n\t1 - Most Profitable Products" +
              "\n\t2 - Least Profitable Products" +
              "\n\t3 - Region Insights" +
              "\n\t4 - Sub-Category Insights" +
              "\n\t5 - State Insights" +              
              "\n\t6 - Top Customers" +
              "\n\t7 - Add New Employee" +
              "\n\t8 - Exit")
        selected = input("Choose a menu #: ").lower().strip()

        #Menu Item selected
        if selected == "1":
            # Opens Most Profitable PRoducts
            Profits_Top.top_ten()
        elif selected == "2":
            # Opens Second Insight Code
            Profits_Bottom.bottom_ten()
        elif selected == "3":
            # Opens Region Insights
            Regions.menu()
        elif selected == "4":
            # Opens Sub-Category Insights
            Category.menu()
        elif selected == "5":
            # Opens State Insights
            States.menu()
        elif selected == "6":
            # Opens Top Customer Insights
            Top_Customers.top_customers()            
        elif selected == "7":
            #Opens Add New Employee Code
            New_Employee.add_employee()
            pause()
        elif selected == "8" or selected == "exit":
            # Exits Loop (and Program)
            program_run = False
        else:
            print("'" + selected + "' is not a valid menu selection. " +
                  "Please enter a numerical value from 1-8.\n")
            pause()


'''Main'''
login_successful = Login.login()

if login_successful == True:
    mainmenu()

print("\nThank you for using Office Solutions Data Analytics." +
      "\nNow Exiting Program.")
