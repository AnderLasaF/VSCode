//Operators in C++: asignation, arithmetic, comparative, logical and bit level

#include <iostream>
using namespace std;

int main(){   //check if a person is old enough to get a driving license

    /*a scholarship will be granted if the marks are higher than 8 or if commuting distance is >20km*/
    
    int calificacion, distancia_centro;

    cout << "Por favor, introduce la calificacion: ";

    cin >> calificacion;

    cout << "Por favor introduce distancia al centro: ";

    cin >> distancia_centro;

    if (calificacion>=8 || distancia_centro>20){  //comparing with lowercase

        cout << "Tienes derecho a beca";
    }
    else{

        cout << "No cumples los requisitos para obtener beca";
    }
}