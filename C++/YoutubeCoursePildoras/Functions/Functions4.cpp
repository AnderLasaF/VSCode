//parameters by default

#include <iostream>
using namespace std;

void mostrarMensaje(string msg, int veces=1){  //default value for optional parameter "veces". Optional parameter has to be at the end

    for (int i=0;i<veces;i++){

        cout << msg << endl;
    }

}

void mostrarMensaje2(string msg="Bienvenidos", int veces="1"){

    for (int i=0;i<veces;i++){

        cout << msg << endl;
    }
   
}


//Another practical example

void crearVentana(int ancho=800, int alto=600, string titulo ="Mi ventana", bool completa=False){

    cout <<"Creando ventana: " << titulo << "\n"

         <<"Ancho: " << ancho << "\n"

         <<"Alto: "  << alto  << "\n"

         <<"Pantalla completa: " << (completa ? "Si":"No") << "\n\n"; 
 
}

int main() {

    mostrarMensaje("Hola alumnos");  //we call the function with only one parameter, veces=1 (default)
    mostrarMensaje("Hola alumnos",7); //veces=7

    mostrarMensaje2(); //takes default values
    mostrarMensaje2("Hasta luego"); //substitute the first parameter
    mostrarMensaje2("Hasta luego",5); //new values
    mostrarMensaje2(,5); //NOT POSSIBLE

    crearVentana(); //takes the default values

}