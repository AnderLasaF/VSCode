//location of dynamic memory. It's devided in 4 parts: 
// 1. Segment of code/text, read only (contains the executable code)
// 2. Segment of data (subdivided into initialized and non initialized data)
// 3. Stack
// 4. Heap

//We are going to focus on the stack and the heap

//stack: call to functions, local variables, what a function gives back with return, etc. Has a limited size and it's configured by default. LIFO type
//heap: dynamic memory asignation. During the execution of the program. The heap is managed by the developer in C++. The size is flexible (dynamic).

//A bad management of the heap can lead to issues (memory leaks, etc)

//we are going to see what happens when a pointer is defined, where is it stored and what happens when that pointer is being used to point to a memory address, etc

#include <iostream>
using namespace std;

int main(){

    int * int_ptr{nullptr};  //if a pointer is not initialized, it can contain whatever value on the memory randomly

    int_ptr = new int; //assigning memory to an integer on the heap (with the word new). The pointer points to that space of memory. The pointer (since it's a variable) is saved in the stack

    cout << int_ptr << endl; //print the memory address where the pointer is pointing (not from the pointer itself)

    cout << &int_ptr << endl; //print the memory address of the pointer 

    int * int_ptr2 = new int; //assigned directly to a memory address on the heap

    *int_ptr2 = 10; //assign a value to the space on memory where the pointer is pointing

    cout << "Valor antes de delete: " << *int_ptr2 << endl;

    delete int_ptr2;  //we are releasing the memory assigned to int_ptr2, which means it can be reused

    cout << int_ptr2 << endl;  //the memory address is still stored, however it's free (hanging pointer). It is adviced to make it point to null

    int_ptr2 = nullptr;


}