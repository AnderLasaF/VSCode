//Used to iterate collections, such as arrays or containers (vector, list, set, map, etc)
//In the for-each loop, we don't know how many times are we going to iterate (intedetermined)
//Some collections may grow during execution time (like a vector)
//This feature was released on C++ 11
//Sintax:    for (declaration : container) { body }

#include <iostream>
using namespace std;

int main(){

    int edades[] {15,25,27,35,95};

    for(int e:edades){    //the variable e has to be the same type as the array edades

        cout << e << endl;
    } 

//lets imagine that we have an array but not the data type of the elements, how we define the variable
//that iterates the elements?? This can be done with inference type with the reserved word "auto"

//its also possible to iterate strings

    string email = "juan@pildorasinformaticas.es";
    
    for(auto e: email){
         
        if(e=='@') cout << "Encontre la @ ";
        else cout << "No la encontre ";
    
    }



}