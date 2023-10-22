# this is inventory.py file. happy


print("Welcome to Programming Principles Sample Product Inventory")

def Is_Number(number):
    num_truth = number.isnumeric()
    if num_truth == False:
        try:
            number = float(number)
            num_truth = True
        except ValueError:
            num_truth = False
    return num_truth



class Product:
    def __init__(self, Product_Name,Curent_Stock, Sale_Price, Manufacture_Cost, Monthly_Production):
        pass

    def set_name_product(Product):
        Product_Name = input("Please enter the Product Name: ")
        Product.Product_Name = Product_Name

    def set_Stock(Product):
        while True:
            Curent_Stock = input("Please enter the current amount in stock: ")
            Number_truth = Is_Number(Curent_Stock)
            if Number_truth == True:
                Product.Curent_Stock = int(Curent_Stock)
                return None
            else: print("please input a proper number.")

    def set_Sale_Price(Product):
        while True:
            Sale_Price = input("Please enter the products price: ")
            Number_truth = Is_Number(Sale_Price)
            if Number_truth == True:
                Product.Sale_Price = float(Sale_Price)
                return None
            else: print("please input a proper number.")

    def set_Manufacture_Cost(Product):
        while True:
            Manufacture_Cost = input("Please enter the cost of manufacturing the product: ")
            Number_truth = Is_Number(Manufacture_Cost)
            if Number_truth == True:
                Product.Manufacture_Cost = float(Manufacture_Cost)
                return None
            else: print("please input a proper number.")

    def set_Monthly_Production(Product):
        while True:
            Monthly_Production = input("Please enter the amount of product made in one month: ")
            Number_truth = Is_Number(Monthly_Production)
            if Number_truth == True:
                Product.Monthly_Production = int(Monthly_Production)
                return None
            else: print("please input a proper number.")



Chair = Product

Chair.set_name_product(Chair)
Chair.set_Stock(Chair)
Chair.set_Sale_Price(Chair)
Chair.set_Manufacture_Cost(Chair)
Chair.set_Monthly_Production(Chair)

print(Chair.Product_Name)
print(Chair.Curent_Stock)
print(Chair.Sale_Price)
print(Chair.Manufacture_Cost)
print(Chair.Monthly_Production)




month_count = 13
while month_count <= 12:
    print("****** Programming Principles Sample Stock Statement******")
    print(" Product Code:")
    print(" Product Name: ", Product_Name)

    print(" Sale Price: ", Sale_Price)
    print(" Manufacture Cost :", Manufacture_Cost)
    print(" Monthly Production: ", Monthly_Production)

    print(" Month:", month_count)
    print(" Manufactured: 100 units")
    print(" Sold: 110 units")
    print(" Stock: 90 units")
    month_count += 1