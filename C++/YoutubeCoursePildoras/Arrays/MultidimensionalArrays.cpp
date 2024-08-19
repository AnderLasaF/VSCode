#include <iostream>
using namespace std;
 
int main(){

    //program that controls month, day and hour in a point where vehicles go through

    int carPassing[24][31][12];      //first dimension 24h, second 31 days and third 12 months

    //15 may 2am

    carPassing[2][14][4]=4;

    cout << "Number of cars the 15th of May at 2 AM are: " << carPassing[2][14][4];

    for (int i=0; i<24; i++){   //0-23h 

        for (int j=0; j<31; j++){  //1-30 days

            for (int z=0; z<12; z++){ //0-11 months

                 carPassing[i][j][z] = rand() % 1000 //random numbers between 0 and 1000. If we want from x to 1000, we add x as an offset       
            }
        }

    }  

cout << "Number of cars 7 November at 19:00 were: " << carPassing[19][6][10];

//there is no exception if we try to access a position from the array which is out of bounds. Ex:  carPassing[19][6][15]. This is known as Undefined Behavior
}