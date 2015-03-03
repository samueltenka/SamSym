<<<Includes>>>
#include <iostream>
using namespace std;
<@ Print: a string @>
<@ Print: a double @>


<<<Print: a string>>>
void print_for_me(const char* string) {
   cout << string << endl;
}

<<<Print: a double>>>
void print_for_me(double x) {
   cout << x << endl;
}
