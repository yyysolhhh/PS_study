#include <iostream>
using namespace std;
int main(void) {
  while (true) {
    int a, b;
    cin >> a >> b;
    if (!a and !b) break;
    if (a > b)
      cout << "Yes\n";
    else
      cout << "No\n";
  }
  return 0;
}