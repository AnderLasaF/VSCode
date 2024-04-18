#include <iostream>  //interaction with the console

/*
Block comment
*/

int addNumbers(int number1, int number2)
{
    int result = number1 + number2;
    return result;
}

//Main function. Starting point of the program
int main(){  

    int first_number {3}; //Statement
    int second_number {7};

    std::cout << "First number: " << first_number << std::endl;
    std::cout << "Second number: " << second_number << std::endl;

    int sum = addNumbers(first_number,second_number);
    std::cout << "Sum: " << sum << std::endl;

    //We can also call the function directly without using a variable for storing the info
    std::cout << "Sum : " << addNumbers(3,42) << std::endl;

    return 0;
}

