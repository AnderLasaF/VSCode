//overloading functions: ability of define multiple functions with the same name but different parameters
//in this way the code can become more legible (summing several number of different data type for instance)
//abstraction, flexibility, polimorfism, reusage of code

//Be CAREFUl overloading functions! The overloaded functions should have a clear relation between them
//Ex: sum (int value1, int value2), sum(float value1, float value2)

#include <iostream>
using namespace std;

//funcion para sumar dos numeros enteros
int sumar(int a, int b){
    return a+b;
}

//funcion para sumar tres numeros enteros
int sumar(int a, int b, int c){
    return a+b+c;
}

//funcion para sumar dos numeros flotantes
float sumar(float a, float b){
    return a+b
}

int valor(int z){
    return 5;
}

double valor(){
    return 5.5;
}

int main(){

    cout << valor() << endl;
    return 0;
}

