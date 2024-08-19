#include <iostream>
using namespace std;

int main(){

    //Bad habits working with pointers

    //Writing into uninitialized pointer through dereference
    int *p_number2; //Contains junks address: could be anything!
    *p_number2 = 55; //Writing into junk address. Bad!
    cout << "Writing into uninitialized pointer through dereference" << endl;
    cout << "p_number2: " << p_number2 << endl;   //Reading from junk address
    cout << "*p_number2 : "  << *p_number2 << endl;

    //The program fails at line 10, when trying to write into an address that can be whatever!


    //Initializing pointer to null ptr and writing on it afterwards
    int *p_number3 {}; //pointing to null
    *p_number3 =33; //writing into a pointer pointing nowhere. Bad!!

    cout << "Reading and writing through nullptr: " << endl; 

    //Dynamic heap memory
    int *p_number4{nullptr};
    p_number4 = new int; //Dynamically allocate space for a single int on the heap. This memory belongs to our program from now on. The system
                         //can't use it for anything else, untill we return it. After this line executes, we will have a valid memory location
                         //allocated. The size of the allocated memory will be such that it can store the type pointed to by the pointer

    *p_number4 = 77; //Writing into dynamically allocated memory
    cout << "Dynamically allocating memory: " << endl;
    cout << "p_number4: " << *p_number4 << endl;
}