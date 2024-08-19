/*
Pass of pointers as parameter. Use cases

1. Modify the original value without returning a value and assigning it without making any copy
2. Working with high amounts of data. It saves time and memory since it's not needed to copy the whole object
3. Work with arrays and strings. Arrays are passed as default as pointers
4. Management of dynamic memory. It makes easier to work with dynamic memory (assigned with new or malloc), allowing that functions modify complex data structures or dynamic arrays

Pass a parameter as reference vs pass a pointer as parameter

Pass parameter by reference: when we want to pass to a function a high load of data as reference (no copies in memory)
Pass pointer as parameter to functions: 
*/

//Function that receives a pointer as parameter and modifies an external variable to the function

#include <iostream>
using namespace std;

void cambiarValor(int* valor){  //pointer as parameter, it expects a memory value

    (*valor)+=5; //increase in 5 the content of the pointer
}


int main(){


    int num=5; 

    cout << "El valor de num antes de llamar a la funcion es: " << num << endl;

    cambiarValor(&num); //memory address of num

    cout << "El valor de num despues de llamar a la funcion es: " << num << endl;
}