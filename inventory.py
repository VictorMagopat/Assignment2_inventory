# This is inventory.py file. Created: 2023.10.19
# Author: Victor Magopat
# This file implements the inventory simulation.
# The product-class is instantiated using user input.
# A simulation is running to estimate sales for 12 months. 
# It prints the annual statement for the profit of the simulation.

# import all moduals
import random
import product

# determines if the variable can be converted to a Float.
def Is_Number(number):
    num_truth = number.isnumeric()
    if num_truth == False:
        try:
            number = float(number)
            num_truth = True
        except ValueError:
            num_truth = False
    return num_truth

# sets the name of the product using user's input
def Enter_Product_Name():
    Product_Name = input("Please enter the Product Name: ")
    Chair.set_Name(Product_Name)

# sets the code associated to the product using user's input
def Enter_Code():
    while True:
        product_code = input("Please enter the code of the product [100 to 1000]: ")
        valid_number = Is_Number(product_code)
        if valid_number == True:
            product_code = int(product_code)
            if product_code <= 1000 and product_code >= 100: 
                Chair.set_Code(int(product_code))
                return None
            else: print("Please enter a number in range 100 to 1000.")
        else: print("Please enter a number in range 100 to 1000.")

# sets the curent stock using user's input
def Enter_Stock():
    while True:
        curent_stock = input("Please enter the current count in stock: ")
        valid_number = Is_Number(curent_stock)
        if valid_number == True:
            Chair.set_Stock(int(curent_stock))
            return None
        else: print("Please input a proper number.")

# sets the sale price of the product using user's input
def Enter_Sale_Price():
    while True:
        sale_price = input("Please enter the products selling price: ")
        valid_number = Is_Number(sale_price)
        if valid_number == True:
            Chair.set_Sale_Price(round(float(sale_price),2))
            return None
        else: print("Please input a proper number.")

# sets the cost to make the product using user's input
def Enter_Manufacture_Cost():
    while True:
        manufacture_cost = input("Please enter the cost of manufacturing the product: ")
        valid_number = Is_Number(manufacture_cost)
        if valid_number == True:
            Chair.set_Manufacture_Cost(round(float(manufacture_cost),2))
            return None
        else: print("Please enter a proper number.")

# sets the amount stock using user's input
def Enter_Monthly_Production():
    while True:
        monthly_production = input("Please enter the amount of product made in one month: ")
        valid_number = Is_Number(monthly_production)
        if valid_number == True:
            Chair.set_Monthly_Production(int(monthly_production))
            return None
        else: print("Please input a proper number.")

# simulates the amount of product sold in a month
def Simulate_Units_Sold(current_stock, production):
    # random number used simulate the units sold 
    sale_variance = random.randint(0, 10)
    # random number used to determined sign (+) or (-)
    variance_state = random.randint(1, 2)
    if variance_state == 1:
        units_sold = production - sale_variance
        if units_sold <= 0:
            units_sold = 0
    elif variance_state == 2:
        units_sold = production + sale_variance
        if units_sold >= current_stock:
            units_sold = current_stock
            print("Stock sold out.")
    else: print ("there was a problem")
    return units_sold

# the application starts here
# instantiate the product Chair
Chair = product.Product()

# set the attributes of the product Chair using the user input
Enter_Product_Name()
Enter_Code()
Enter_Stock()
Enter_Sale_Price()
Enter_Manufacture_Cost()
Enter_Monthly_Production()

# print the product attributes
print("****** Programming Principles Sample Stock Statement******")
print(" Product Code:", Chair.Code)
print(" Product Name: ", Chair.Name)

print(" Sale Price: ", Chair.Sale_Price)
print(" Manufacture Cost :", Chair.Manufacture_Cost)
print(" Monthly Production: ", Chair.Monthly_Production)
print("Welcome to Programming Principles Sample Product Inventory")

# accumulates the profit over the-12 month period
accrued_profit = 0

# stores the units sold that month
units_sold = 0

# index of the month in process
month_index = 1

# the number of the months in one year
months_in_year = 12

while month_index <= months_in_year:
    print("____________________________________________")
    print(" Month:", month_index)
    print(" Manufactured: " + str(Chair.Monthly_Production) + " units")

    # update the stock with the month of production.
    Chair.Stock += Chair.Monthly_Production

    units_sold = Simulate_Units_Sold(Chair.Stock, Chair.Monthly_Production)
    print(" Sold: "+ str(units_sold) + " units")

    # update the stock after a month of selling the product.    
    Chair.Stock -= units_sold

    print(" Stock: "+ str(Chair.Stock) + " units")

    # calculates the net profit for that month and adds it to the total profit
    accrued_profit += (units_sold * Chair.Sale_Price) - (Chair.Monthly_Production * Chair.Manufacture_Cost)
    month_index += 1

# This prints the statment of the yearly profit
print("The total profit for the 12 month period is: ", round(accrued_profit, 2))