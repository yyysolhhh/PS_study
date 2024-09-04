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
  int a_zero = A.length() - 1;
  int b_zero = B.length() - 1;
  if (op == '+') {
    if (a_zero == b_zero) {
      cout << '2';
      print_zero(a_zero);
    } else {
      int big = max(a_zero, b_zero);
      int small = min(a_zero, b_zero);
      cout << '1';
      print_zero(big - small - 1);
      cout << '1';
      print_zero(small);
    }
  } else if (op == '*') {
    cout << 1;
    print_zero(a_zero + b_zero);
  }
  return 0;
}