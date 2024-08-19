/*
Dangling pointer: Pointer that doesn't point to a valid memory address. Dereferencing a dangling pointer will result in undefined behavior
There are 3 kinds of dangling pointers: 
        1. Uninitialized pointer. SOLUTION: Always initialize your pointers
        2. Deleted pointer. SOLUTION: Reset pointers after delete
        3. Multiple pointers pointing to the same memory. SOLUTION: For multiple pointers to same address, make sure the owner pointer is very clear

*/

#include <iostream>
using namespace std;

int main(){

    //Case1: Uninitialized pointer
    int *p_number;   //Dangling uninitialized pointer. Case1

    cout << "Case 1: Uninitialized pointer: ." << endl;
    cout << "p_number : " << p_number << endl;
    cout << "*p_number : " << *p_number << endl;  //CRASH!!
    
    //Case2: Deleted pointer
    int *p_number1 {new int{67}};

    cout << "*p_number1 (before delete) : " << *p_number1;

    delete *p_number1;   //Deleted memory, it does not "belong" to us anymore

    cout << "*p_number1(after delete) : " << *p_number1 << endl;   //we can't dereference it


    //Case3: Multiple pointers pointing to the same address

    int *p_number3 {new int{83}};
    int *p_number4 {p_number3};   //both pointers pointing to the same direction

    cout << "p_number3 - " << p_number3 << " - " << *p_number3 << endl;
    cout << "p_number4 - " << p_number4 << " - " << *p_number4 << endl;

    //Deleting p_number3
    delete p_number3;

    //p_number4 points to deleted memory. Dereference it will lead to undefined behaviour: Crash/garbe or whatever
    cout << "p_number4 (after deleting p_number3) - " << p_number4 << " - " << *p_number4 << endl; 


    //Solution1: Initialize pointers immediately upon declaration
    int *p_number5{nullptr};
    int *p_number6{new int{56}};

    //Check for nullptr before use!
    if(p_number6!=nullptr){
        cout << "*p_number6 : " << *p_number6 << endl;
    }
}