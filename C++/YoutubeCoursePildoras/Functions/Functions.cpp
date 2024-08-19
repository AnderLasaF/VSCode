//Where to find a summary of the C++ functions: cppreference.com

#include <iostream>
using namespace std;
#include <cmath>

double elevaPotencia(double base, double exponente){

    return pow(base,exponente)

}

int main(){

    cout << "El resultado es: " << elevaPotencia(5,3);   
    
}