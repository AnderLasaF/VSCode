#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

void ejemploFuncion(int num){  //Pass of parameter by value. The original value (introduced as parameter) does not change

    num = 50;
}

void ejemploFuncion2(int &num){ //Pass of parameter by reference (&). The original value changes to the one in the function

    num = 50;
}

void duplicarElementos(vector<int> &vec){ //modify the original vector, not a copy

    for(int &valor:vec){  //we need to include & in valor, otherwise it will create a copy of every value in the vector

        valor*=2;
    }

}

int main(){

    int minum = 10;
    cout << "Valor original" << minum << endl; //original value is 10

    ejemploFuncion(minum);  //the value of minum is stored in num, but minum does not change
    cout << "Valor despues de llamar a la funcion: " << minum << endl;
    //this is know as pass by value in C++. In the background it means that a copy of minum is passed
    //as a parameter to the ejemploFuncion function.

    ejemploFuncion2(minum);  //pass by reference
    cout << "Valor despues de llamar a la funcion 2: " << minum << endl; 

    
    //Another example
    vector <int> numeros={1,2,3,4,5};  //we need to modify the original values multiplying them by 2
    
    cout << "Valores originales: ";

    for(int valor:numeros){

        cout << valor << " ";
    }
    cout << endl;

    duplicarElementos(numeros);

    cout << "Valores despues de llamar a la funcion: ";

    for(int valor: numeros){

        cout << valor << " ";
    }

    cout << endl;
}

//When do we use each case?

//Cases that not require to modify the original value: Function that calculate the square of a number
//Cases that require to modify the original value: Function that resets a value.
//When working with data structures or big classes, copy all the object might be inneficient. Pass by reference avoid the copy
//Polimorfism: is common to pass object by reference (or pointers) 