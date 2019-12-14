"""
State Insights
Purpose: Called from Main. Shows insights to user based on states

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def pause():
    input("Press 'Enter' to continue...")

def get_year():
    #User supplied Year
    year_range = False
    while year_range == False:
        num = False
        while num == False:
            year = input("Enter a year of interest (2014-2017): ")
            if year.isdigit() == True:
                year = int(year)
                num = True
            else:
                print("Invalid Year Format. Please enter a number between 2014 and 2017")
                continue
            if year >= 2014 and year <= 2017:
                year_range = True
            else:
                print("Invalid Year. Please choose a year between 2014 and 2017")
    return year

def get_month():
    #User supplied Month
    month_range = False
    while month_range == False:

        num = False
        while num == False:
            month = input("Enter a month of interest (1–12): ")
            if month.isdigit() == True:
                month = int(month)
                num = True
            else:
                print("Invalid month format. Please enter a number between 1 and 12.")
                continue
            if month >= 1 and month <= 12:
                month_range = True
            else:
                print("Invalid month. Please choose a month between 1 and 12.")
    return month

def get_quarter():
    #User supplied Quarter
    quarter_range = False
    while quarter_range == False:

        num = False
        while num == False:
            quarter = input("Enter a quarter of interest (1–4): ")
            if quarter.isdigit() == True:
                quarter = int(quarter)
                num = True
            else:
                print("Invalid quarter format. Please enter a number between 1 and 4.")
                continue
            if quarter >= 1 and quarter <= 4:
                quarter_range = True
            else:
                print("Invalid quarter. Please choose a quarter between 1 and 4.")
    return quarter

def get_profit_sales(column_sort, start_date, end_date, asc=False):
    #Returns states by specified column sort
    xl = pd.ExcelFile("SalesDataFull.xlsx")
    data = xl.parse("Orders")

    data = data[(data['Order Date'] >= start_date) & (data['Order Date'] < end_date)]

    col_prof = data[["Order Date","State",column_sort]]
    col_profits = col_prof.groupby(["State"]).sum().sort_values(by=[column_sort], ascending=asc)
    col_profits = col_profits.reset_index()

    return col_profits

def state_profit_sales(selection):
    #Sub Menu for scope of display
    sub_menu = False
    while sub_menu == False:
        print("Please choose a display option:" +
            "\n\t1 - All Years" +
            "\n\t2 - Individual Year" +
            "\n\t3 - Individual Month" +
            "\n\t4 - Individual Quarter")
        option = input("Choose a display option #: ").lower().strip()

        if option == "1":
            #Data for all years
            state_data = get_profit_sales(selection,"2014","2018")
            scope = ""
            sub_menu = True
        elif option == "2":
            # Data for specific year
            year = get_year()
            state_data = get_profit_sales(selection,str(year),str(year+1))
            scope = " for " + str(year)
            sub_menu = True
        elif option == "3":
            # data for specific month
            year = get_year()
            start_month = get_month()
            if start_month < 12:
                end_month = start_month+1
                end_date = str(year) + '-' + str(end_month) + '-01'
            else:
                end_date = str(year+1)

            start_date = str(year) + '-' + str(start_month) + '-01'
            state_data = get_profit_sales(selection,start_date,end_date)
            scope = " for " + str(start_month) + '/' + str(year)
            sub_menu = True
        elif option == "4":
            # data for specific quarter
            year = get_year()
            quarter = get_quarter()

            if quarter == 1:
                start_date = str(year)
                end_date = str(year) + '-' + '4'
            elif quarter == 2:
                start_date = str(year) + '-' + '4'
                end_date = str(year) + '-' + '7'
            elif quarter == 3:
                start_date = str(year) + '-' + '7'
                end_date = str(year) + '-' + '10'
            elif quarter == 4:
                start_date = str(year) + '-' + '10'
                end_date = str(year+1)

            state_data = get_profit_sales(selection,start_date,end_date)
            scope = " for Quarter " + str(quarter) + " in " + str(year)
            sub_menu = True
        else:
            print("'" + option + "' is not a valid option selection." +
                "Please enter a numerical value from 1-4\n")
            pause()

    def formatfunc(*args, **kwargs):
        #Formatting for postive and negative $ amounts
        value = args[0]
        if value >= 0:
            return '${:,.2f}'.format(value)
        else:
            return '-${:,.2f}'.format(abs(value))

    with pd.option_context('display.float_format', formatfunc):
        print(selection + " by State " + scope)
        print(state_data)

        # Bar Chart
        chart = sns.barplot(x=selection, y="State", data=state_data)
        chart.set_title(selection + " by State " + scope)
        chart.figure.set_size_inches(12, 8)
        chart.figure.tight_layout()
        plt.show()

def menu():
    menu_loop = True

    while menu_loop == True:
        print("\nState Insights")
        print("Please choose a display option:" +
             "\n\t1 - Sales by State" +
             "\n\t2 - Profits by State" +
             "\n\t3 - Quantity Sold by State" +
             "\n\t4 - Return to Main Menu")
        selected = input("Choose an option #: ").lower().strip()

        #Option selected
        if selected == "1":
            # Selected Sales by state
            state_profit_sales("Sales")
            pause()
        elif selected == "2":
            # Selected Profits by state
            state_profit_sales("Profit")
            pause()
        elif selected == "3":
            # Individual Year - By Month
            state_profit_sales("Quantity")
            pause()
        elif selected == "4" or selected == "return" or selected == "exit":
            # Return to Main Menu
            menu_loop = False
        else:
            print("'" + selected + "' is not a valid menu selection." +
                 "Please enter a numerical value from 1-5\n")
            pause()

'''For Testing'''
#menu()
