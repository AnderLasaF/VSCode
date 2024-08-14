//vector: class of the std library of C++. They can grow/decrease dynamically (unlike arrays). Vector class has multiple useful methods (size, etc)
//they store elements (from the same type) in memory next to each other or separated through pointers

#include <iostream>
#include <vector>
using namespace std;

int main(){

    int k;

    vector <int> records (5);   //predefined size, not needed. Value 0 by default

    vector <char> letras {'z', 'w', 'r'};

    vector <double> salario_base (350,2125.50);  //350 elements with value 2125.50

    for (int i=0; i<5; i++){

        cout << records[i] << endl; 
    }

//sometimes it'll be more useful to use a while loop to go through a vector (if it's undetermined)
//if the size of the vector changes, the while loop would still work (also if we use the size
//in the for loop)


//in case we'd need a while loop:

    int j = 0;

    while(j<salario_base.size()){
        cout << salario_base[j]<<endl;
        j++;
    }
}