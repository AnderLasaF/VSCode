#include <iostream>  //interaction with the console

/*
We want to see compile time errors
*/

//Main function. Starting point of the program
int main(){  

    //Compile time error (deleting the semicolon)
    std::cout << "Hello World!" << std::endl;
    
    //Run time error. Generates warning intead of error, but the .exe file is possible to be executed
    int value = 7/0;

    //However, the program will not show the following line of code
    std::cout << "value: " << value << std::endl;
    return 0;
}

//After we compile the program we can see that rooster.exe has been generated. If we run it through the terminal, we'll see the output of our code