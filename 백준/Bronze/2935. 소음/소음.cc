#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  string A, B;
  char op;
  cin >> A >> op >> B;
  int a_digit = A.length();
  int b_digit = B.length();
  if (op == '+') {
    if (a_digit == b_digit) {
      int zero = a_digit - 1;
      cout << '2';
      while (zero--) cout << 0;
    } else {
      int big = max(a_digit, b_digit);
      int small = min(a_digit, b_digit);
      for (int i = big; i > 0; i--) {
        if (i == big || i == small)
          cout << '1';
        else
          cout << '0';
      }
    }
  } else if (op == '*') {
    int zero = a_digit + b_digit - 2;
    cout << 1;
    while (zero--) cout << 0;
  }
  return 0;
}