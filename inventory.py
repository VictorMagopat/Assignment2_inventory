# this is inventory.py file. happy
# import all moduals
import random
import product

# Determine if the variable can be turned into a Int or Float.
def Is_Number(number):
    num_truth = number.isnumeric()
    if num_truth == False:
        try:
            number = float(number)
            num_truth = True
        except ValueError:
            num_truth = False
    return num_truth

# sets a name of the product to the object
def Enter_Product_Name():
    Product_Name = input("Please enter the Product Name: ")
    Chair.set_Name(Product_Name)

# sets a code associated to the product to the object
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

# sets the curent stock of the product to the object
def Enter_Stock():
    while True:
        curent_stock = input("Please enter the current count in stock: ")
        valid_number = Is_Number(curent_stock)
        if valid_number == True:
            Chair.set_Stock(int(curent_stock))
            return None
        else: print("Please input a proper number.")

# sets the sale price of the product to the object
def Enter_Sale_Price():
    while True:
        sale_price = input("Please enter the products selling price: ")
        valid_number = Is_Number(sale_price)
        if valid_number == True:
            Chair.set_Sale_Price(float(sale_price))
            return None
        else: print("Please input a proper number.")

# sets the cost to make the product to the object
def Enter_Manufacture_Cost():
    while True:
        manufacture_cost = input("Please enter the cost of manufacturing the product: ")
        valid_number = Is_Number(manufacture_cost)
        if valid_number == True:
            Chair.set_Manufacture_Cost(float(manufacture_cost))
            return None
        else: print("Please enter a proper number.")

# sets the amount stock made  of the product to the object
def Enter_Monthly_Production():
    while True:
        monthly_production = input("Please enter the amount of product made in one month: ")
        valid_number = Is_Number(monthly_production)
        if valid_number == True:
            Chair.set_Monthly_Production(int(monthly_production))
            return None
        else: print("Please input a proper number.")

# simulates the amount of product sold in a month.
def Stock_Sold(current_stock):
    number_sold = random.randrange(0, current_stock)
    return number_sold

# calculates the stock remaining after a month of selling the product.
def Find_Stock_Remaining(current_stock, number_sold):
    remaining_stock = current_stock - number_sold
    return remaining_stock

# calculates the stock after the month of production.
def Stock_Production(current_stock, stock_produced):
    total_stock = current_stock + stock_produced
    return total_stock

# calculates the cost of producing more products for every month
def Cost_Of_Production(monthly_production, manufacture_cost):
    monthly_cost = monthly_production * manufacture_cost
    return monthly_cost

# calculates the revenue for the month, subtracts the cost and then adds the previos months profit
def Total_Profit(number_sold, sale_price, monthly_cost, profit):
    revenue = number_sold * sale_price
    profit = revenue - monthly_cost + profit
    return profit

Chair = product.Product()

Enter_Product_Name()
Enter_Code()
Enter_Stock()
Enter_Sale_Price()
Enter_Manufacture_Cost()
Enter_Monthly_Production()


print("****** Programming Principles Sample Stock Statement******")
print(" Product Code:", Chair.Code)
print(" Product Name: ", Chair.Name)

print(" Sale Price: ", Chair.Sale_Price)
print(" Manufacture Cost :", Chair.Manufacture_Cost)
print(" Monthly Production: ", Chair.Monthly_Production)
print("Welcome to Programming Principles Sample Product Inventory")


profit = 0
month_count = 1
while month_count <= 12:
    print("____________________________________________")
    print(" Month:", month_count)
    print(" Manufactured: " + str(Chair.Monthly_Production) + " units")
    sold = Stock_Sold(Chair.Stock)
    print(" Sold: "+ str(sold) + " units")
    Chair.Stock = Find_Stock_Remaining(Chair.Stock, sold)
    Chair.Stock = Stock_Production(Chair.Stock, Chair.Monthly_Production)
    print(" Stock: "+ str(Chair.Stock) + " units")
    monthly_cost = Cost_Of_Production(Chair.Monthly_Production, Chair.Manufacture_Cost)
    profit = Total_Profit(sold, Chair.Sale_Price, monthly_cost, profit)
    month_count += 1


print("the total profit was: ", profit)