//methods in vectors (they are thought to work dynamically with vectors)
//at(): access a specific element in a specific position. Checks for bounds limits
//push_back(): add elements to a vector

#include <iostream>
#include <vector>
using namespace std;

int main(){

    vector <int> records {25,45,60,35};   //predefined size, not needed. Value 0 by default

    vector <char> letras {'z', 'w', 'r'};

    vector <double> salario_base (350,2125.50);  //350 elements with value 2125.50

    int i=0;

    cout << records.at(3); //same result as records[3], but it checks the limits of the vector

    //if we try to access to a position that does not exist we get an out of range exception
    //cout << records.at(7);

    records.at(3) = 105;
    cout << records.at(3);

    //if we want to add another element to the records vector:

    records.push_back(105);  //added to the end (like .append)

    for (int i=0; i<records.size(); i++){

        cout << records.at(i) << endl;
        
    }
    }
