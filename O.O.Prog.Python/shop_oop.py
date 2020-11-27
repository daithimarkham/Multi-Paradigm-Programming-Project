import csv

class Product: # Simple class containing a name and a price.

    def __init__(self, name, price=0): # when you don't know price, defaults value to zero. Assume price is 0 if not put in.
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f'NAME: {self.name} PRICE: {self.price}' # Returns name and the price

class ProductStock: # has a product and a quantity 
    
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def name(self): # Name of product
        return self.product.name
    
    def unit_price(self): # Returns price of product
        return self.product.price

    # Use this when refer to what customer wants to buy, or q in shop.  
    # If we want to change something later, we can do it here in this one place. 
    def cost(self): # works best when want to know q in shop, how much price is. 
        return self.unit_price() * self.quantity
        
    def __repr__(self): # Returns product and quantity.
        return f"{self.product} QUANTITY: {self.quantity}" # **self is an instance of class which calls product class.**

class Customer:

    def __init__(self, path): # method, called constructor, called when object created from class.
        self.shopping_list = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader) # pulls in info about itself from csv
            self.name = first_row[0] # name from first row
            self.budget = float(first_row[1]) # budget, self is pulling in an individual instance of a customer.
            for row in csv_reader: # 
                name = row[0]
                quantity = float(row[1])
                p = Product(name)
                ps = ProductStock(p, quantity)
                self.shopping_list.append(ps) # prod and prod stock that are being added to a shopping list,
                # inside customer class. declared on line 33.
                
    def calculate_costs(self, price_list): # method passes in stock array, and comes in with price list for all stock.
        for shop_item in price_list: #  for loop for all stock, 
            for list_item in self.shopping_list: # then an inner loop, for every item in shop, check it against what I want to buy.
                if (list_item.name() == shop_item.name()): # if 2 names are same, 
                    list_item.product.price = shop_item.unit_price() # save price of shop items into customer instances, and cal cost.
    
    def order_cost(self): # 
        cost = 0
        
        for list_item in self.shopping_list: # for every item in our shooping list,
            cost += list_item.cost() # we go through and get the cost of that item, and total the cost. 
        
        return cost # return total.
    
    def __repr__(self):
        
        str = f"{self.name} wants to buy" # gets name of customer, wants to buy
        for item in self.shopping_list: # iterate through for loop in shopping list
            cost = item.cost() # call method to calculate cost of item
            str += f"\n{item}" # repr method, name of item
            if (cost == 0): # if cost = 0, 
                str += f" {self.name} doesn't know how much that costs :(" # name of customer and prints
            else:
                str += f" COST: {cost}"
                
        str += f"\nThe cost would be: {self.order_cost()}, he would have {self.budget - self.order_cost()} left"
        return str 
        
class Shop:
    
    def __init__(self, path): # Constructer, path to csv file, where info needed to set up shop will be.
        self.stock = [] # Create blank array to keep our stock in. 
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.cash = float(first_row[0]) # Set our cash value to be coming from 1st row.
            for row in csv_reader:
                p = Product(row[0], float(row[1])) # Create products 
                ps = ProductStock(p, float(row[2])) # Create productStock
                self.stock.append(ps) # Put them into our stock inside this class.
    
    def __repr__(self): # repr method 
        str = "" # Creates string 
        str += f'Shop has {self.cash} in cash\n' # Appends info to that string.
        for item in self.stock: # Loops through all the product stock in array stock, through self which we created.
            str += f"{item}\n" # Returns that info about item, line by line. How much, how many left etc.
        return str # returns string about everything in shop

s = Shop("stock.csv")
#print(s)

c = Customer("customer.csv")
c.calculate_costs(s.stock)
print(c)