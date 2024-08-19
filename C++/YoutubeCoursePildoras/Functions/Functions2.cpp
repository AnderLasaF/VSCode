//A prototype function is a previous declaration of a function that informs the compilator that 
//it will be used in the program, as well as it's data type, parameters and if the function returns
//a value or not. Due to convention they are defined in the beginning of the program. They can be
//defined in external files (with extensions .h or .hpp)

#include <iostream>
using namespace std;
#include <cmath>

double elevaPotencia(double base, double exponente); //prototype function. Informs the compiler that we
//are going to use at some point a function double elevaPotencia(double base, double exponente)

int main(){

    cout << "El resultado es: " << elevaPotencia(5,3);   
    
}


double elevaPotencia(double base, double exponente){

    return pow(base,exponente)

}

//if we would like the function not to return anything, as an example that the result is just shown
//in the terminal, we would have to define the function as void and remove the return:

void elevaPotencia(double base, double exponente){

    cout << pow(base,exponente);
}
