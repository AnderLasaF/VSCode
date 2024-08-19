//Useful in applications that have to run continuously and other situations

#include <iostream>
#include <thread>
#include <chrono>
using namespace std;


double leerTemperatura(){

    return 20.0 + (rand() % 20);   //number between 20 and 39.9
}

//programacion concurrente: varios hilos a la vez (uno en primer plano y otros en segundo plano)

void esperarSegundos(int segundos){

    this_thread::sleep_for(chrono::seconds(segundos))
}

int main(){

    const double LIMITE_TEMPERATURA=35.0;

    while(true){  //infinite loop that keeps calling the leerTemperatura method/function

        double tempActual = leerTemperatura();
        cout << "Temperatura actual: " << tempActual << " C" << endl;

        if(tempActual>LIMITE_TEMPERATURA){

            cout << "ALERTA!! Temperatura limite alcanzada: " << tempActual << " C" << endl;
        }
        esperarSegundos;

    }
}