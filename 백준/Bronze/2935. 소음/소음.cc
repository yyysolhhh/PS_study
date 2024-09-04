#include <bits/stdc++.h>
using namespace std;
void print_zero(int n) {
  while (n--) cout << '0';
}
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
      cout << '2';
      print_zero(a_digit - 1);
    } else {
      int big = max(a_digit, b_digit);
      int small = min(a_digit, b_digit);
      cout << '1';
      print_zero(big - small - 1);
      cout << '1';
      print_zero(small - 1);
    }
  } else if (op == '*') {
    cout << 1;
    print_zero(a_digit + b_digit - 2);
  }
  return 0;
}