/*Arrays and pointers
In C++ an array is a pointer to the first element of the array.

The value of the name of the array is the memory address of the first element of the array.

When the name of the array is used without any index, the memory address of the first element is obtained

When a pointer points to the same data type than the elements of the array, in almost every scenario, it can
be used the name of the pointer or the name of the array to perform similar operations, specially about 
indexation and pointer arithmetic. However there are some exceptions
*/

/*
The pointer arithmetic is a relevant concept in C and C++. Allows to perform arithmetic operations over pointers.
Pointers are variables that store memory addresses and the arithmetic is used to calculate memory addreesses, 
which allows to acess and manipulate data in different possitions of an array or memory block.

With pointer we can perform the following operations:

- Increment (++): When incrementing a pointer, it's value is increased to point to the next element of an array. The
increment is performed in terms of the size of the data type that the pointer is pointing to. For example, if a pointer is
"int" type (assuming int has a syze of 4 bytes), when the pointer is increased it will point 4 bytes further in memory, which
means, to the next element of the pointer.

- Decrement (--): Similar to increment, but in the other direction. When decrementing a pointer, it points to the previous
element in an array.

- Sum (+): It's possible tu sum an integer to a pointer so that the pointer moves on several elements in an array. As well
as with the increment, the sum is calculated multiplying the integer number times the size of the data type that the pointer points to

- Substraction (-): It's possible to subtract an integer to a pointer to move the pointer backwards in an array. It's also possible
to subtract two pointers to obtain the difference between them, as long as both pointers point to elements within the same array
*/

#include <iostream>
using namespace std;

int main(){

    int cifras[]={10,20,30};  //array of type integer with 3 elements
    
    cout << cifras << endl;  //if we print the name of the array, we get the memory address of the first element

    cout << *cifras << endl;  //we are accessing the value saved in the memory address. 10 in this case

    //we create a pointer that points to the array, in order to see that we get the same result as before
    int *ptr_cifras {cifras};

    cout << ptr_cifras << endl; //print the pointer, we get the memory address of the array cifras
 
    cout << *ptr_cifras << endl; //print the value of the pointer, we get the first element of the array cifras

    cout << ptr_cifras[0] << endl; //first value of the array

    cout << (ptr_cifras+1) << endl; //access to the next memory possition in the array, of the second element

    cout << *(ptr_cifras+1) <<endl; //second value of the array


}

