//auto return: automatic deduction of the return data type of a function (introduced in C++ 14)
//example: 

auto suma(int a, int b){  //dummy example
    return a+b;
}

//this is specially useful to simplify the code writing and while working with difficult data types or with blueprints

#include <iostream>
using namespace std;

auto suma(int a, int b){

    return a + b;
}

int main(){

    int x=5, y=3;

    int resultado = suma(x,y);

    cout << "La suma de " << x << " y " << y << " es: " << resultado;

}

//use cases: working with complex types, generics, deep nested, lambda functions, OOP (type defined by the developer), conditional returns

template <typename T, typename U> //generic types 
auto suma(T a, U b){  //this is where also auto becomes useful
    return a+b;
}

int main(){
-
    //use with int
    auto sum1 = suma(5,3);
    cout << "Suma de enteros: " << sum1 << endl;

    //use with int and float
    auto sum2 = suma(5, 2.5);
    cout << "Suma de entero y flotante: " << sum2 << endl;

    return 0;
}