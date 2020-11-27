#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Product {
	char* name;
	double price;
};

struct ProductStock {
	struct Product product;
	int quantity;
};

struct Shop {
	double cash;
	struct ProductStock stock[20];
	int index;
};

struct Shop createAndStockShop()
{

FILE * fp; // fp = file pointer,
char * line = NULL;
size_t len = 0;
ssize_t read;

fp = fopen("stock.csv", "r"); // r = read, w = write, rw = read write to csv file //
if (fp == NULL) // IF FILE DOESNT EXIST //
exit(EXIT_FAILURE);

read = getline(&line, &len, fp);
float cash = atof(line);
//printf("cash in shop is %.2f\n", cash);

struct Shop shop = {cash};

while ((read = getline(&line, &len, fp)) != -1) // keep reading file, line by line, until end //
{
//printf("%s IS A LINE", line);
char *n = strtok(line, ",");
char *p = strtok(NULL, ","); // null is special character,
char *q = strtok(NULL, ",");
int quantity = atoi(q);
double price = atof(p);
char *name = malloc(sizeof(char) * 50);
strcpy(name, n); // dynamically allocate new memory to save name, avoid strtok error
struct Product product = { name , price };
struct ProductStock stockItem = { product, quantity };
shop.stock[shop.index++] = stockItem; // add stock to shop as an array
// printf("NAME OF PRODUCT %s PRICE %.2f QUANTITY %d\n" , name, price, quantity);
}
return shop;
}

double find(struct Shop s, char* name)
{
	for (int i = 0; i < s.index; i++)
	{
		if (strcmp(name, s.stock[i].product.name) == 0){
			return s.stock[i].product.price;
		}
	}
	return -1;
}

int main(void) 
{
	struct Product productA = { "Coke Can", 0.0 };
	struct Product productB = { "Big Bags", 0.0 };
	struct Product productC = { "Spaghetti", 0.0 };
	struct ProductStock StockA = { productA, 12 }; // Customer wants 12 Coke Cans
	struct ProductStock StockB = { productB, 5 }; // Cus wants 5 Big Bags
	struct ProductStock StockC = { productC, 2 }; // Cus wants 2 Spaghetti
	
	struct ProductStock array[] = { StockA, StockB, StockC }; // WE WILL USE POINTER
	
	struct Shop shop = createAndStockShop(); // reads in shop
	
	double totalCostForCustomer = 0; // Total cost for all customer products, 
    // done outside the loop when all products are named and required by customer,
    // and then code line 82, and print it on line 84 then. 
	for(int i=0; i < 3; i++){ // For loop 
		struct Product p = array[i].product; // Finds products in array
		double price = find(shop, p.name); // Finds name and price
		printf("The price of %s in the shop is %.2f\n", p.name, price); // Prints 
		double totalCostOfItem = array[i].quantity * price; // finds out total cost of products
		printf("You want %d of %s, that will cost you %.2f\n", array[i].quantity, p.name, totalCostOfItem); // Tell how much you need for product.
		totalCostForCustomer += totalCostOfItem; // Totals 
	}
	printf("The total cost for the customer will be %.2f\n", totalCostForCustomer);
	
    return 0;
}