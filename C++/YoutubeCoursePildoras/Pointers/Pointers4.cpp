/*
Pointers and constants

1. Pointers to constants: A pointer that points to a constant. This means that the value that is pointing to can't be modified
via the pointer, although the pointer can change and point to another direction.

2. Constant pointer: A pointer whose memory address can't change after initialization. However, the value that is pointing to
can change unless it is a constant.

3. Constant pointer that points to a constant: A pointer that can't change neither the memory address that is pointing to nor the 
content of the value in the memory address

*/

#include <iostream>
using namespace std;

int main(){

    //1.Pointer to constant
    
    const int edad=10;

    const int salario=2500;

    const int *ptr=&edad; //ptr points to the value of edad

    //*ptr=20; this is not possible since the pointer points to a constant!!! It does not compile

    ptr=&salario; //ptr points to where salario is located

    cout << *ptr;  //prints the content of salario

    
    //2.Contant pointer

    int edad2=10;

    int* const ptr2=&edad2; //constant pointer, it has to be initialized

    *ptr2=20; //it's possible to change the value of edad2 through the pointer since edad2 is a variable


    //3. Constant pointer that points to a constant

    const int edad3=10;

    const int* const ptr3=&edad3; //first const means that the pointer points to a constant, second one that the pointer is a constant pointer  
    
    
}