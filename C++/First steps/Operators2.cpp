#include <iostream>
using namespace std;



int main(){

    //exercise that will show if two diff data types interact with a operator, they (and the result) will be converted to the one with more precision (and bigger)
    int a=3;
    float b=4.0f;  //f at the end to indicate that it's float type
    double c=8.0;

    //c++ allows to know which is the most suitable data type for a variable based on the saved value with the special word "auto"

    //auto a=3;

    auto result=a+b;

    cout << "The value of result is: " << result << endl;
    cout << "Data type of result is: " << typeid(result).name() << endl;   //prints the first letter of the data type

    double div = a/2; //the output data type is int, since all the involved values are int, even if we specified to store the value as double

    cout << "The value of div is: " << div << endl;
    cout << "Data type of div is: " << typeid(div).name();
}