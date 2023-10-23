# this is product.py file. 
import random

class Product:
# all the variabls that are attached to the product
    def __init__(self, Name = "Unknown", Code = 100, Stock = 0, Sale_Price = 0, Manufacture_Cost = 0, Monthly_Production = 0):
        self.Name = Name
        self.Code = Code
        self.Stock = Stock
        self.Sale_Price = Sale_Price
        self.Manufacture_Cost = Manufacture_Cost
        self.Monthly_Production = Monthly_Production
        pass

# built in function that changes the Name.
    def set_Name(self, NewName):        
        self.Name = NewName

# built in function that changes the Code.
    def set_Code(self, NewCode):
        self.Code = NewCode

# built in function that changes the current stock
    def set_Stock(self, NewStock):
        self.Stock = NewStock

# built in function that changes the sale price of the product
    def set_Sale_Price(self, NewSalePrice):
        self.Sale_Price = NewSalePrice

# built in function that changes the cost of manufacturing the product
    def set_Manufacture_Cost(self, NewManufactureCost):
        self.Manufacture_Cost = NewManufactureCost

# built in function that changes the total amount of product made that month
    def set_Monthly_Production(self, NewMonthlyProduction):
        self.Monthly_Production = NewMonthlyProduction


