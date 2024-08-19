//the do-while loop makes sure that the loop is at least executed once (unlike the while loop)

#include <iostream>
using namespace std;

int main(){

    int opcion;

    do{

        cout << "Menu de opciones:\n";

        cout << "1. Opcion 1\n";

        cout << "2. Opcion 2\n";

        cout << "3. Salir\n";

        cin >> opcion;

        if(opcion!=3){
            
            cout << "Has elegido la opcion " << opcion << ".\n";
        }

    }while (opcion!=3);

    cout << "Has elegido salir";
    
}