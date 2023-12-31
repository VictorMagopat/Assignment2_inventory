# this is the product.py file. Created: 2023.10.19
# Author: Victor Magopat
# Contains the implementation the class Product.

import random

class Product:
# all the variables that are attached to the product
    def __init__(self, Name = "Unknown", Code = 100, Stock = 0, Sale_Price = 0, Manufacture_Cost = 0, Monthly_Production = 0):
        self.Name = Name
        self.Code = Code
        self.Stock = Stock
        self.Sale_Price = Sale_Price
        self.Manufacture_Cost = Manufacture_Cost
        self.Monthly_Production = Monthly_Production
        pass

# this function sets the Name of the product.
    def set_Name(self, NewName):        
        self.Name = NewName

# this function set the Code of the product.
    def set_Code(self, NewCode):
        self.Code = NewCode

# this function sets the current stock.
    def set_Stock(self, NewStock):
        self.Stock = NewStock

# this function sets the sale price of the product.
    def set_Sale_Price(self, NewSalePrice):
        self.Sale_Price = NewSalePrice

# this function sets the cost of manufacturing the product.
    def set_Manufacture_Cost(self, NewManufactureCost):
        self.Manufacture_Cost = NewManufactureCost

# this function sets the total amount of product made that month.
    def set_Monthly_Production(self, NewMonthlyProduction):
        self.Monthly_Production = NewMonthlyProduction

