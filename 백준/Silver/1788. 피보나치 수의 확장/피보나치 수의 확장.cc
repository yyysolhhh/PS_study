#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  if (n < 0) {
    n = -n;
    if (n % 2 == 0)
      cout << -1;
    else
      cout << 1;
  } else if (n == 0) {
    cout << 0;
  } else {
    cout << 1;
  }
  int fibonacci[n + 1];
  fibonacci[0] = 0;
  fibonacci[1] = 1;
  for (int i = 2; i <= n; i++) {
    fibonacci[i] = (fibonacci[i - 2] + fibonacci[i - 1]) % 1000000000;
  }
  cout << '\n' << fibonacci[n];
  return 0;
}