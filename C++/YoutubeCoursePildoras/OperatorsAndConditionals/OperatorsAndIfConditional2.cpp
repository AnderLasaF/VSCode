//Operators in C++: asignation, arithmetic, comparative, logical and bit level

#include <iostream>
using namespace std;

//convert string to lowercase
void toLowerCase(string &cadena){  //value "cadena" by reference and not value

    for(int i=0; i<cadena.length(); i++){

        cadena[i] = tolower(cadena[i]);
    }

}

int main(){   //check if a person is old enough to get a driving license

    int edad;

    string ex_medico;

    cout << "Por favor introduce tu edad: ";

    cin >> edad;

    cout << "Has pasado el examen medico (Si/No)?: ";  //C++ is case sensitive. Convert to lowercase or uppercase

    cin >> ex_medico;

    toLowerCase(ex_medico);

    if (edad>=18 && ex_medico=="si"){  //comparing with lowercase

        cout << "Puedes obtener el carnet de conducir";
    }
    else{

        cout << "No cumples los requisitos";
    }
}