//Fundamental in C++ that allows an efficient and detailed memory management and other hardware resources. Pointers are variable whose main function is to store memory addresses.
//In those memory addresses stored by pointers there can be: primitive types, arrays, classes, another pointer, functions, dynamic block of memory, reserved block of memory, etc.
//Principal pointers applications: direct access and modification of the memory. Creation of dynamic functions and data structures. Pass of parameters by reference. Arrays and strings. Low level programming

//Advantages using pointers: direct control of memory, flexibility on data structures usage, interaction with hardware on low level, pass of parameters by reference, compatibility with C.
//Advantages of not using pointers: more simplicity on development, more security, less worried about memory failures

#include <iostream>
using namespace std;

int var2 = 15;

void miFuncion(int var2){

    var2 = var2+10;  //we are not modifying var2

}

void miFuncionPuntero(int * var2){  //we're modifying var2 directly, more efficient than doing it with a copy

    * var2 = * var2 + 10;
}

int main(){

    miFuncion(var2); 

    miFuncionPuntero(&var2); //physical memory of var2
    
    cout << var2 << endl;  //it has not been modified

    int var = 10;

    int * ptr; //pointer that will contain an integer data type

    ptr = &var; //store in the pointer ptr the memory direction of the variable var

    cout << var << endl;  //print the value of var

    cout << &var << endl; //print the memory address of var

    cout << ptr << endl;  //print the memory address of var saved in the pointer

    cout << *ptr << endl; //print the pointed value by ptr

    *ptr = 55; //modify the value of var through the pointer ptr

    cout << var << endl;   
}