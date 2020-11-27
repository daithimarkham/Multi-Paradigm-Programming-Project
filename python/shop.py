# David Markham 05/11/2020
# Write a Python file in procedural language, and read in a CSV file to it.

from dataclasses import dataclass, field
from typing import List
import csv

# Create Classes 
@dataclass
class Product:
    name: str
    price: float = 0.0 

@dataclass
class ProductStock:
    product: Product
    quantity: int 

@dataclass
class Shop:
    cash: float = 0.0 # default value for cash
    stock: List[ProductStock] = field(default_factory=list) # when a new shop,
    # is created use default_factory which built in Python, to gen new list.
    # we don't have to declare a new list all the time.

@dataclass
class Customer:
    name: str = ''
    budget: float = 0.0
    shopping_list: List[ProductStock] = field(default_factory=list) # creates list when list is created.

# Function to read in STOCK CSV file.
def create_and_stock_shop():
    s = Shop()
    with open('stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader) # prints first row from csv file
        s.cash = float(first_row[0]) # convert to float for product, decimals.
        for row in csv_reader:
            p = Product(row[0], float(row[1])) 
            ps = ProductStock(p, float(row[2])) 
            s.stock.append(ps)
            # print(ps)
    return s 

# Function to read in Customer CSV file.
def read_customer(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',') 
        first_row = next(csv_reader)
        c = Customer(first_row[0], float(first_row[1])) 
        for row in csv_reader:
            name = row[0]
            quantity = float(row[1])
            p = Product(name) 
            ps = ProductStock(p, quantity)
            c.shopping_list.append(ps) 
        return c 
        
        

# function print out info for user.
def print_product(p):
    print(f'\nPRODUCT NAME: {p.name} \nPRODUCT PRICE: {p.price}') 

def print_customer(c):
    print(f'CUSTOMER NAME: {c.name} \nCUSTOMER BUDGET: {c.budget}')

    for item in c.shopping_list: 
        print_product(item.product)

        print (f'{c.name} ORDERS {item.quantity} OF ABOVE PRODUCT')
        cost = item.quantity * item.product.price 
        print(f'The cost to {c.name} will be €{cost}')

def print_shop(s):
    print(f'Shop has {s.cash} in cash')
    for item in s.stock:
        print_product(item.product) 
        print(f'The shop has {item.quantity} of the above.') 

#s = create_and_stock_shop() # setting function to be callled.
#print_shop(s) 

c = read_customer("customer.csv")  
print_customer(c) 








        





