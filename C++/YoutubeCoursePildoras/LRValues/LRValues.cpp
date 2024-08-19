/*
L values: Left values. Expression that represents a location on memory. This means that a L value has a memory location associated. They can appear on the left side of an asignation. 
They can be modified. It might include variables, references and pointer dereference
R values: right values. Expression that represents a temporary value that has no memory location. Data that is on the right of an asignation.
They can't appear on the left side of an asignation (except in references to R-values or with movements).
Temporary and usually destroyed at the end of the expression that appears on
*/

#include <iostream>
#include <utility> //For std::move

using namespace std;

void funcion(int &x){  //x is an L value

    x+=5;
}

void funcion2(int &&x){  //funcion2 is expecting a R value

    x+=5;
}

string miFuncion(string &&z){  //R value

    z+=" texto anadido";  //concatenate text

    return move(z);  //returns R value, which means that we are emptying the content of s1 (Ctrl+X)
}

string miFuncion2(string &&z){  //R value

    z+=" texto anadido";  //concatenate text

    return z;  //returns L value, which means we are returning a copy (Ctrl+C)
}

int main(){

    int z = 15; //z is the L value (it's on the left). 15 is the R value

    funcion(z); //call to funcion. In this case z=20
    
    //the method move() converts a L value into a R value
    funcion2(move(z));   

    int b = z;  //b is the L value. Z is a L value assesed as a R value

    cout << "El valor de z es: " << z;


    //Another example

    string s1="Hola alumnos";
    string s2=move(s1);  //convert s1 into a R value. We are moving the content of s1 to s2 (as if doing a Ctrl+X -> Ctrl+V. Without move it's like Ctrl+C -> Ctrl+V)

    //This allows to move content that we have in memory from one place to the other instead of doing copies. 

    cout << "El contenido es: " << s1 << endl;
    cout << "El contenido es: " << s2;


    string s3=miFuncion(s1);
    string s4=miFuncion2(s1);

}