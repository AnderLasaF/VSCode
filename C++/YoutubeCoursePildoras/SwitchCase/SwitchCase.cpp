//In C++ switch-case only work comparing integer types (int, char, long, etc). Not for strings (only with a hash structure)

#include <iostream>
using namespace std;

int main(){

    int opcion;

    cout << "Menu de opciones:"<<endl;
    cout << "1. Mostrar mensaje:"<<endl;
    cout << "2. Calcular una suma:"<<endl;
    cout << "3. Salir del programa"<<endl;
    cout << "Introduce la opcion deseada (1, 2 o 3): "<<endl;

    cin >> opcion;

    switch (opcion)  //a and b are declared within the keys of the switch instruction. They can be used in line 47 if we want
    {
    case 1:

        cout << "Hola alumnos de C++" << endl;
        break;
    
    case 2:
        
        int a,b;

        cout <<"Introduce dos numeros enteros: ";

        cin >> a >> b;

        cout << "La suma de " << a << " y " << b << " es: " << (a+b);

        break;

    case 3:

        cout << "Saliendo del programa";

        break;

    default:
        
        cout << "Opcion de menu no valida";
        break;

    }

}