#include <iostream>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  while (true) {
    int a, b;
    cin >> a >> b;
    if (!a && !b) break;
    if (b % a == 0)
      cout << "factor\n";
    else if (a % b == 0)
      cout << "multiple\n";
    else
      cout << "neither\n";
  }
  return 0;
}