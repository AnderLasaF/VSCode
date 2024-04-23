#include <iostream>
using namespace std;

int main(){

    int matrix[] {15,20,25};  //index starts at 0

    cout << matrix[1] << endl; //prints index 1 of matrix

    int ages[10] {15,20,25}; //array of length 10 with 3 defined elements, the rest are 0

    //it is possible to have a constant as the definer of the lenght for an array\

    const int length{10};

    int ages2[length] {15,20,25};

    ages2[7] = 8;   //assign value in a specific place: the data type has to be the same as the array

    ages2[1] = 32; //we have overwritten the value in position 1

    cin >> ages2[1];  //ask to the user the data for position 1 of ages2 array

    cout << ages2[1];

}