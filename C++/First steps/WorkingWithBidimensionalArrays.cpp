#include <iostream>
using namespace std;

int main(){

    int mi_matriz [4][5] = {15, 25, 8, -7, 92, 77, 12, 11, 7, 44, 56, 59, 43, 78, 12, 43, 95, 12, 87, 33};

    mi_matriz[0][2] = 125;   //rewrite
    cout << mi_matriz[0][2]; 

    int mi_matriz2 [4][5];

    for (int row=0; row <4; row++){

        for (int column=0; column<5; column++){

            cin >> mi_matriz2[row][column];
        }

    }

cout << "Values of the array" << endl;

for (int row=0; row <4; row++){

        for (int column=0; column<5; column++){

            cout << mi_matriz2[row][column];
        }

    cout << endl;   //next line, so we see all the values in a row
    }

}

