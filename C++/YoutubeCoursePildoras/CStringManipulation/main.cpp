#include <iostream>
using namespace std;
#include <cstring>

int main(){

    //Real arrays and those decayed into pointers
    const char message1[] {"The sky is blue."};
    

    //Array decays into pointer when we use const char
    const char* message2 {"The sky is blue."};
    cout << "message 1: " << message1 << endl;



}