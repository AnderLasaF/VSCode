//Inline functions: functions whose body is in the same place as the call of the function
//when an inline function is declared, the compiler tries to expand the code of the function where is called instead of a normal call

//the main use of inline functions is to reduce the resources that are used to call a function, which is useful for small and extensively used functions
//since being the body at the same place of the function call, the overload associated to calling functions is gone (such as argument parsing)

//the sintax is the same as for usual functions except for the reserved word "inline" in front of the function

//advantages: performance optimization, less execution time and the compiler chooses to apply the inline function or not
//disadvantages: impact in the size of the code (after compiling, binary code), that is why modern compilers decide if the function will be inline or not

#include <iostream>
using namespace std;

inline int sumar(int a, int b){

    return a+b;
}

int main(){

    int x=5, y=3;

    int resultado = sumar(x,y);
    //internally (if the function is treated as inline) the call (sumar(x,y)) is being replaced with return a+b

    cout << "La suma de " << x << " y " << " es: " << resultado;


}