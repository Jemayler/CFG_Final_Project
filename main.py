import csv

print("READING THE DATA FROM THE SPREADSHEET" + "\n")

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(row)

print("\n")

print("SALES AND MONTHS" + "\n")

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    sales = []
    for row in spreadsheet:
        sale = int(row['sales'])
        sales.append(sale)
    print("List of sales: {}".format(sales))

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    months = []
    for row in spreadsheet:
        month = str(row['month'])
        months.append(month)
    print("List of months: {}".format(months))

    print("Total sales: £{}".format(sum(sales)))
    print("Highest month sales: £{} in the month of {}".format(max(sales), months[sales.index(max(sales))]))
    print("Lowest month sales: £{} in the month of {}".format(min(sales), months[sales.index(min(sales))]))
    print("Range of monthly sales: {}".format(max(sales) - min(sales)))
    print("Average monthly sales: £{}".format(round((sum(sales) / len(sales)), 2)))

print("\n")

print("PERCENTAGE CHANGE OF SALES BETWEEN MONTHS" + "\n")

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    month_1 = input("Which is the first month you wish to compare? (write in full with capital letter to start) ")
    if month_1 == "January":
        x = sales[0]
    elif month_1 == "February":
        x = sales[1]
    elif month_1 == "March":
        x = sales[2]
    elif month_1 == "April":
        x = sales[3]
    elif month_1 == "May":
        x = sales[4]
    elif month_1 == "June":
        x = sales[5]
    elif month_1 == "July":
        x = sales[6]
    elif month_1 == "August":
        x = sales[7]
    elif month_1 == "September":
        x = sales[8]
    elif month_1 == "October":
        x = sales[9]
    elif month_1 == "November":
        x = sales[10]
    elif month_1 == "December":
        x = sales[11]

    month_2 = input("Which is the second month you wish to compare? (write in full with capital letter to start) ")
    if month_2 == "January":
        y = sales[0]
    elif month_2 == "February":
        y = sales[1]
    elif month_2 == "March":
        y = sales[2]
    elif month_2 == "April":
        y = sales[3]
    elif month_2 == "May":
        y = sales[4]
    elif month_2 == "June":
        y = sales[5]
    elif month_2 == "July":
        y = sales[6]
    elif month_2 == "August":
        y = sales[7]
    elif month_2 == "September":
        y = sales[8]
    elif month_2 == "October":
        y = sales[9]
    elif month_2 == "November":
        y = sales[10]
    elif month_2 == "December":
        y = sales[11]

    print("% change between {} and {}: {}%".format(month_1, month_2, round((((y - x) / x) * 100), 2)))

print("\n")

print("CALCULATIONS WITH THE EXPENDITURE VALUES" + "\n")

with open("sales.csv","r") as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    expenditure = []
    for row in spreadsheet:
        monthly_expenditure= int(row["expenditure"])
        expenditure.append(monthly_expenditure)
    print("Total expenditure: £{}".format(sum(expenditure)))
    print("Highest month expenditure: £{} in the month of {}".format(max(expenditure), months[expenditure.index(max(expenditure))]))
    print("Lowest month expenditure: £{} in the month of {}".format(min(expenditure), months[expenditure.index(min(expenditure))]))
    print("Range of expenditure: {}".format(max(expenditure)-(min(expenditure))))
    print("Average monthly expenditure: £{}".format(round(sum(expenditure)/(len(sales)), 2)))

print("\n")

print("% PROFIT" + "\n")

with open("sales.csv","r")as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    month = input("Which month do you want to calculate % profit for? (write in full with capital letter to start) ")
    if month == "January":
        x = expenditure[0]
        y = sales[0]
    elif month == "February":
        x = expenditure[1]
        y = sales[1]
    elif month == "March":
        x = expenditure[2]
        y = sales[2]
    elif month == "April":
        x = expenditure[3]
        y = sales[3]
    elif month == "May":
        x = expenditure[4]
        y = sales[4]
    elif month == "June":
        x = expenditure[5]
        y = sales[5]
    elif month == "July":
        x = expenditure[6]
        y = sales[6]
    elif month == "August":
        x = expenditure[7]
        y = sales[7]
    elif month == "September":
        x = expenditure[8]
        y = sales[8]
    elif month == "October":
        x = expenditure[9]
        y = sales[9]
    elif month == "November":
        x = expenditure[10]
        y = sales[10]
    elif month == "December":
        x = expenditure[11]
        y = sales[11]
    print("% profit for {}: {}%".format(month, round(((y - x) / x) * 100), 2))

print("\n")

print("GRAPHS USING PANDA (big extension)" + "\n")

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("sales.csv")
print(df)
print(df.info())
a=df["sales"].min()
b=df["sales"].max()
c=df["sales"].median()
d=df["sales"].mean()
e=df["sales"].sum()
f=df["expenditure"].sum()
print("Maximum monthly sales £{}, Minimum monthly sales £{}. Range of monthly sales {}".format(b,a,b-a))
print("Median monthly sales £{}".format(round(c), 2))
print("Average monthly sales £{}".format(round(d)))
print("Total sales £{}. Total expenditure £{}".format(e,f))
print("Percentage profit for 2018 {}%".format(round(((e-f)/f)*100),2))
df=pd.read_csv("sales.csv")

# line graph of month against sales and expenditure
df.plot(kind="line",x="month")
plt.show()
# bar graph showing sales per month
df.plot(kind="bar",x="month",y="sales")
plt.show()
# bar graph showing expenditure per month
df.plot(kind="bar", x="month",y="expenditure")
plt.show()
# scatter graph showing the relationship between months and sales
df.plot(kind="scatter", x="month", y="sales")
plt.show()
# scatter graph showing the relationship between expenditure and sales
df.plot(kind="scatter", x="expenditure",y="sales")
plt.show()