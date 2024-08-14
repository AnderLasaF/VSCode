#include <iostream>
using namespace std;

int main(){

    int a=5;

    int b=5;

    int z=++a;  //incrementing a in one unit as prefix

    cout << "El valor de z es: " << z << endl;

    cout << "El valor de a es: " << a << endl;

    int w=b++; //incrementing as suffix. First assign the value of b to w, then b is incremented
    //the code is read from left to right

    cout << "El valor de w es: " << w << endl;

    cout << "El valor de b es: " << b << endl;
    
    
    //a+=b; //a = a+b (a = 5+10)

    //same goes for -=, *=, /=

    //cout << "The value of a is " << a <<endl;
}