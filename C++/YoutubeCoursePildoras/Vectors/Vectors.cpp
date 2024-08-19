//Class of the std library of C++. It can store sequential data. They can grow/decrease dynamically (unlike arrays). There are plenty of methods available to work with vectors
//It is possible to store data in separated memory addresses, which they are accessible through pointers. Data has to be from the same data type. First index is 0, last size-1

#include <iostream>
#include <vector>
using namespace std;

int main(){

    vector  <int> records (5); //fixed length of the vector. Not an empty vector (0 as default)

    vector <char> letras (10); //Undetermined characters as initial values

    //fill the salary for 350 workers. They'll have the same base value
    vector <double> base_salary (350,2125.50); //length of 350 and value of 2125.50 for all the positions of the vector

    //if the vector has an undertermined size, a for loop is not the best approach to go over it, the while loop it does
    vector <char> letras2 ('a','b','c','d','e');
    
    int i=0;
    while(i<base_salary.size()){

        cout << base_salary[i] << endl;
        i++;
    }

    for (int i=0; i<350; i++){

        cout << base_salary[i] << endl;
    }
}