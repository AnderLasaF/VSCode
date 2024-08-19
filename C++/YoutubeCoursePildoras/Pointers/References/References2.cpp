#include <iostream>
#include <string>
using namespace std;

//Example of references. Exchange the value of two variables through a function

void intercambio(int &a, int &b){ //parameters by reference (&), every change made to "a" and "b" will affect the referenced values
 
    int temp=a; //temporary variable
    
    a=b;

    b=temp;
}

void intercambioConPunteros(int *a, int *b){  //also possible to do it with pointers, but the syntax is more complex

    int temp = *a;
    *a = *b;
    *b = temp;
}

void incrementarNoNulo(int *valor){  //increment the value valor if the original value is not Null

    if(valor!=nullptr){

        *valor++;
    }

}


int main(){

    int var1=10;
    
    int var2=20;

    cout << "Antes del intercambio: var1= " << var1 << " var2= " << var2 << endl;
 
    intercambio(var1,var2);
    intercambioConPunteros(&var1, &var2); //feeding memory addresses

    //after exchange

    cout << "Despues del intercambio: var1= " << var1 << " var2= " << var2 << endl;

    //another example. In this case we can ONLY work with pointers

    int a=5;
    int *b=nullptr;
    incrementarNoNulo(&a);
    incrementarNoNulo(b); //null

    cout << "Valor de a: " << a << endl;

    
}