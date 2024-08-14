#include <iostream>    //directive: allows to add content from libraries
using namespace std;
                       /*specifies that we are going to use the space of names standard (std) which allows to avoid 
                       //collisions for functions etc. with the same name but different behavior (concept of virtual 
                       spaces*/

int main(){ //every c++ program will start execution in the main function

    cout << "Hola alumnos que tal" << endl;   //cout belongs to <iostream>. Shows message in console
    //console out
    //endl: goes to the next line
    //if we get rid of "using namespace std" in line two, we have to specify std::cout and std::endl in line 9

    return 0;   //every sentence has to finish with semicolon ;
     
}
 