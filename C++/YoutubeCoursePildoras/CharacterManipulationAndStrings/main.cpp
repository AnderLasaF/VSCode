/*C-Strings are not convenient or safe to work with on C++. C++ provides a type std::string
*/

#include <iostream>
using namespace std;




int main(){
    

    //Check if character is alphanumeric
    //isalnum returns !=0 if the value is alphanumeric and 0 otherwise
    cout << "Is alphanumeric: " << endl;
    cout << "'C' is alphanumeric: " << isalnum('C') << endl;
    cout << "'^' is alphanumeric: " << isalnum('^') << endl;

    //Check if character is alphabetic
    //isalpha returns !=0 if the value is alphabetic and 0 otherwise
    cout << "C is alphabetic: " << isalpha('C') << endl;
    cout << "^ is alphabetic: " << isalpha('^') << endl;
    cout << "7 is alphabetic: " << isalpha('7') << endl;

    //Check if a character is blank
    char message[] {"Hello there. how are you doing? The sun is shining."};
    cout << "message: " << message << endl;

    //Find and print blank index
    int blank_count{};
    for (size_t i{0};i<size(message);i++){
        if(isblank(message[i])){
            cout << "Found a blank character at index: [" <<  i << "]" <<endl;
            blank_count++; 
        }
    }
    cout << "In total we found " << blank_count << " blank characters." << endl;


    //Check if a character is lowercase or uppercase

    char thought[] {"The C++ Programming Language is one of the most used on the Planet"};
    size_t lowercase_count{};  //more appropiate (unsigned integer) than int since the variable is used as a counter 
    size_t uppercase_count{};

    //Print original string for ease of comparsion on the terminal
    cout << "Original string : " << thought << endl;

    for(auto character : thought){  //we use auto since there will be different types of characters (int, string, etc)
        if(islower(character)){
            lowercase_count++;
        }
        if(isupper(character)){
            uppercase_count++;
        }
    }
    cout << "Found " << lowercase_count << " lowercase characters and " << uppercase_count << " uppercase characters" << endl;
    
    
    //Check if a character is a digit
    char statement[] {"Mr Hamilton owns 221 cows. That's a lot of cows! The kid exclamed."};
    cout << "statement: " << statement << endl;

    size_t digit_count{};

    for(auto character: statement){
        if(isdigit(character)){
            cout << "Found digit: " << character << endl;
            digit_count++;
        }
    }

    cout << "Found " << digit_count << " digits in the statement string" << endl;
    
    //Turning a character to lowercase using the tolower() function

    char original_str[] {"Home. The feeling of belonging"};
    char dest_str[size(original_str)];

    //Turn to uppercase. Change the array in place
    for(size_t i{}; i<size(original_str),i++){
        dest_str[i]= toupper(original_str[i]);
    }

    cout << "Original string: " << original_str << endl;
    cout << "Uppercase string: " << dest_str << endl;


    //Turn to lowercase. Change the array in place
    for(size_t i{}; i<size(original_str);i++){
        dest_str[i] = tolower(original_str[i]);
    }
    cout << "Lowercase string: " << dest_str << endl;
    return 0;
}

