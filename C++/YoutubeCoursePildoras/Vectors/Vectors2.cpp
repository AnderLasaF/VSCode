#include <iostream>
#include <vector>
using namespace std;

//Methods to work dinamically with vectors: at(), push.back()

int main(){

    vector  <int> records (5); //fixed length of the vector. Not an empty vector (0 as default)

    vector <char> letras (10); //Undetermined characters as initial values

    //fill the salary for 350 workers. They'll have the same base value
    vector <double> base_salary (350,2125.50); //length of 350 and value of 2125.50 for all the positions of the vector

    //if we access to a position that does not exist, we'll get an unexpected result (from a different memory address, allocate memory)
    cout << records(7);  

    //with the at() method it checks if the boundaries are out of range. It wil throw an exception or error
    cout << records.at(7);

    //same if we are assigning a specific value, an exception will be thrown
    records.at(8) = 206;

    //push back appends a value at the end of the vector
    records.push_back(32); //store 32 at the end of the vector, in a new position

    //we can also use a for loop to iterate the vector if we make use of the .size() method:
    for(int i=0; i<records.size(); i++){
        cout << records.at(i)<<endl;
    }


}

