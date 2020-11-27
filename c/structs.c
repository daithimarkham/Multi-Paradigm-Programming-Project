// Week 6 - Structs Explained
// Struct is a datatype, made up of other datatypes. 

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Way of grouping variables together in a structure.
struct A {
	int val;
	double val2;
	int val3;
};

struct B {
	struct A aInsideB;
};

// Here we access the variable we created in the struct.
void printA(struct A a){
	printf("this is 'val' %d, this is 'val2' %.2f, and this is 'val3' %d\n", a.val, a.val2, a.val3);
}

int main(void) 
{
	struct A a = { 10, 20.2, 4 }; // Here we are creating a new instance of that struct. Store integers in struct. 10 goes into val, and so on.
	printA(a);
	struct A a2 = { 100 }; // Here we can just pu in one value, 100 into 1st variable.
	printA(a2);
	
	struct B b = { a }; // Can pass it via a method like above, but when we print, we use b.aInsideB 
	printA(b.aInsideB);
	
	struct A a3 = b.aInsideB;
	printf("this is a 'val' (%d) from the A which is inside the B", a3.val); // Get struct a, which is inside b, and call val which is 10.

    return 0;
}