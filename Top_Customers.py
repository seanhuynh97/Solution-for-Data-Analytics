"""
Customer Insights
Purpose: Called from Main. Shows top customers for a specified time period

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def pause():
    input("Press 'Enter' to continue...")

def print_data(data,data_title,chart_title):
    #Prints dataframe and displays chart
    def formatfunc(*args, **kwargs):
        #Formatting for positive and negative $ amounts
        value = args[0]
        if value >= 0:
            return '${:,.2f}'.format(value)
        else:
            return '-${:,.2f}'.format(abs(value))

    with pd.option_context('display.float_format', formatfunc):
        print(data_title)
        print(data)
        
    chart = sns.barplot(x="Sales", y="Customer Name", data=data)
    chart.set_title(chart_title)
    chart.figure.set_size_inches(12, 8)
    chart.figure.tight_layout()
    plt.show()
        
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

def top_ten_by_year():
    #Get top 10 customers by year
    excel = pd.ExcelFile("SalesDataFull.xlsx")
    order_data = excel.parse("Orders")

    order_year = order_data["Order Date"].dt.year
    order_data["Year"] = order_year

    columns = order_data[['Year', 'Customer Name', 'Sales']]
    profit = columns.groupby(['Year', 'Customer Name']).sum().sort_values(by='Sales', ascending=False)
    profit = profit.reset_index()
    profit = profit.sort_values(by=['Sales', 'Year'], ascending=False)

    year = get_year()

    select_year = profit.loc[profit['Year'] == year]
    
    data_title = "\nTop 10 Customers of " + str(year) + ":\n "
    chart_title = "Top 10 Customers of " + str(year)
    
    print_data(select_year.head(10), data_title, chart_title)    

def top_ten_by_year_month():
    #Get top ten customers by month
    excel = pd.ExcelFile("SalesDataFull.xlsx")
    order_data = excel.parse("Orders")

    order_year = order_data["Order Date"].dt.year
    order_data["Year"] = order_year

    month = order_data["Order Date"].dt.month
    order_data["Month"] = month

    columns = order_data[['Year', 'Month', 'Sales', 'Customer Name']]
    profit = columns.groupby(['Year', 'Month', 'Customer Name']).sum().sort_values(by='Sales', ascending=False)
    profit = profit.reset_index()

    year = get_year()
    month = get_month()

    select_year_month = profit.loc[(profit['Year'] == year) & (profit['Month'] == month)]

    data_title = "\nTop 10 Customers of " + str(month) + "/" + str(year) + ":\n"
    chart_title = "Top 10 Customers of " + str(month) + "/" + str(year) + ": "
    
    print_data(select_year_month.head(10), data_title, chart_title)

def top_ten_by_year_quarter():
    #Get top ten customers by quarter
    excel = pd.ExcelFile("SalesDataFull.xlsx")
    order_data = excel.parse("Orders")

    order_year = order_data["Order Date"].dt.year
    order_data["Year"] = order_year

    quarter = order_data["Order Date"].dt.quarter
    order_data["Quarter"] = quarter

    columns = order_data[['Year', 'Quarter','Sales', 'Customer Name']]
    profit = columns.groupby(['Year', 'Quarter', 'Customer Name']).sum().sort_values(by='Sales', ascending=False)
    profit = profit.reset_index()

    year = get_year()
    quarter = get_quarter()

    select_year_quarter = profit.loc[(profit['Year'] == year) & (profit['Quarter'] == quarter)]

    data_title = "\nTop 10 Customers of Quarter " + str(quarter) + " in " + str(year) + ":"
    chart_title = "Top 10 Customers of Quarter " + str(quarter) + " in " + str(year) + ":"
    
    print_data(select_year_quarter.head(10), data_title, chart_title)

def top_ten_all():
    #Get top ten customers for all years
    xl = pd.ExcelFile("SalesDataFull.xlsx")
    data = xl.parse("Orders")

    data = data[(data['Order Date'] >= "2014") & (data['Order Date'] < "2018")]

    col_prof = data[["Order Date","Customer Name","Sales"]]
    col_profits = col_prof.groupby(["Customer Name"]).sum().sort_values(by=["Sales"], ascending=False)
    col_profits = col_profits.reset_index()

    data_title = "\nTop 10 Customers:\n"
    chart_title = "Top 10 Customers"
    
    print_data(col_profits.head(10), data_title, chart_title)

def top_customers():
    #Menu display for Top Customers
    profit_loop = True
    while profit_loop == True:
        print("\nTop Customers")
        print("Please choose a display option:" +
            "\n\t1 - All Years" +
            "\n\t2 - Individual Year" +
            "\n\t3 - Individual Year - By Month" +
            "\n\t4 - Individual Year - By Quarter" +
            "\n\t5 - Return to Main Menu")
        selected = input("Choose a menu #: ").lower().strip()

        if selected == "1":
            top_ten_all()
            pause()
        elif selected == "2":
            top_ten_by_year()
            pause()
        elif selected == "3":
            top_ten_by_year_month()
            pause()
        elif selected == "4":
            top_ten_by_year_quarter()
            pause()
        elif selected == "5" or selected == "return" or selected == "exit":
            profit_loop = False
        else:
            print("'" + selected + "' is not a valid menu selection." +
                "Please enter a numerical value from 1-5\n")
            pause()

'''For Testing'''
#top_customers()
