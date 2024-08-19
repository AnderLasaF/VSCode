//recursive functions: function that calls to itself during execution until it reaches a base case, or there will be a stack overflow. Example: factorial of a number
//sometimes recursion is less efficient that a loop, but the code is more legible (usually) with recursion

#include <iostream>
using namespace std;


int factorial(int n){

    if (n==0){

        return 1;  //base case
    }else{
        return n* factorial(n-1);  //recursivity
    } 
}
//example with n=5 --> return 5 * factorial(5-1) 
//n=4              --> return 4 * factorial(4-1)
//n=3              --> return 3 * factorial(3-1)
//n=2              --> return 2 * factorial(2-1)
//n=1              --> return 1 * factorial(1-1)
//n=0              --> return 1 = factorial (1-1) (it goes back and return the call of factorial(1-1) and so on)

int main(){

    int numero;
    cout << "Introduce un numero: " << endl;

    cin >> numero;

    cout << factorial(numero);
}