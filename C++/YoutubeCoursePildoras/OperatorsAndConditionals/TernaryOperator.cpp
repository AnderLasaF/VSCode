//Ternary/conditional operator. Recommended to be used when the conditions to check are simple.
//"?" "text to show if true":"text to show if false"

#include <iostream>
using namespace std;

int main(){

    int num {};

    cout << "Introduce un num entero: ";
    
    /*
    cin >> num;

    if (num%2==0){

        cout << num << " es par" << endl;
    }
    else{

        cout << num << " es impar " << endl;
    }
    */
    
    //all this can be simplified with the ternary operator

    string resultado = (num%2==0)?" es par":" es impar";

    cout << num << " es " << resultado; 


}