#include <stdio.h> // File with extensions, C function declarations, shared between several sources files, 
// such as below:
#include <string.h> // Defines Defines core input and output functions
#include <stdlib.h> // Standard library for C

// Void method
void askName()
{
    fflush(stdin); // Fflush clears input stream,
    printf("What is your name?\n");
    char name[10];
    fgets(name,10,stdin); // Gets a name from standard input.
    printf("Glad to meet you %s\n",name);
}

int main(void)
{
    int choice = -1;

    while (choice != 0) {

        fflush(stdin); // Fflush clears input stream, stdin is standard input.
        printf("\nPlease choose an option ");
        scanf("%d", &choice); // Gets a number from user

        if (choice == 1)
        {
            printf("The user pressed 1\n");
        }  else if (choice ==2){
            printf("Here we can do something else");
        } else if (choice ==3){
            askName(); // Call method we created for user name.
        }
    }
    printf("Bye"); 
}