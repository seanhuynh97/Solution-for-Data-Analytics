"""
Region Insights
Purpose: Called from Main. Shows insights to user based on regions
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
    #Returns Regions by specified column sort
    xl = pd.ExcelFile("SalesDataFull.xlsx")
    data = xl.parse("Orders")

    data = data[(data['Order Date'] >= start_date) & (data['Order Date'] < end_date)]

    col_prof = data[["Order Date","Region",column_sort]]
    col_profits = col_prof.groupby(["Region"]).sum().sort_values(by=[column_sort], ascending=asc)
    col_profits = col_profits.reset_index()

    return col_profits

def region_profit_sales(selection):
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
            region_data = get_profit_sales(selection,"2014","2018")
            scope = ""
            sub_menu = True
        elif option == "2":
            # Data for specific year
            year = get_year()
            region_data = get_profit_sales(selection,str(year),str(year+1))
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
            region_data = get_profit_sales(selection,start_date,end_date)
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

            region_data = get_profit_sales(selection,start_date,end_date)
            scope = " for Quarter " + str(quarter) + " in " + str(year)
            sub_menu = True
        else:
            print("'" + option + "' is not a valid option selection." +
                "Please enter a numerical value from 1-4\n")
            pause()

    def formatfunc(*args, **kwargs):
        #Formatting for positive and negative $ amounts
        value = args[0]
        if value >= 0:
            return '${:,.2f}'.format(value)
        else:
            return '-${:,.2f}'.format(abs(value))

    with pd.option_context('display.float_format', formatfunc):
        print("Region " + selection + " Insights" + scope)
        print(region_data)

    def make_autopct(values,selection):
        #Formatting for Pie Chart % and display values
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))

            if selection == "Quantity":
                return '{p:.0f}% \n {v:,.0f}'.format(p=pct,v=val)
            else:
                return '{p:.0f}% \n ${v:,.0f}'.format(p=pct,v=val)
        return my_autopct

    if selection == "Profit":
        # Bar Chart due to possible negative values
        chart = sns.barplot(x=selection, y="Region", data=region_data)
        chart.set_title("Regional " + selection + scope + ":")
        plt.show()
    else:
        # Pie chart for sales and quantity
        region_data.index = region_data["Region"]
        pie = region_data.plot.pie(y=selection, autopct=make_autopct(region_data[selection],selection), shadow=False, legend=None, figsize=(7,7))
        pie.set_title("Regional " + selection + scope + ":")
        plt.show()

def menu():
    #Menu display for Region Insights
    menu_loop = True

    while menu_loop == True:
        print("\nRegion Insights")
        print("Please choose a display option:" +
            "\n\t1 - Sales by Region" +
            "\n\t2 - Profits by Region" +
            "\n\t3 - Quantity Sold by Region" +
            "\n\t4 - Return to Main Menu")
        selected = input("Choose an option #: ").lower().strip()

        #Option selected
        if selected == "1":
            # Selected Sales by Region
            region_profit_sales("Sales")
            pause()
        elif selected == "2":
            # Selected Profits by Region
            region_profit_sales("Profit")
            pause()
        elif selected == "3":
            # Individual Year - By Month
            region_profit_sales("Quantity")
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
