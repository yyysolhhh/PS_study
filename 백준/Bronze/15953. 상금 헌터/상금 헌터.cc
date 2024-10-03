#include <bits/stdc++.h>
using namespace std;
int festival1(int a) {
  if (a == 0)
    return 0;
  else if (a == 1)
    return 5000000;
  else if (a <= 3)
    return 3000000;
  else if (a <= 6)
    return 2000000;
  else if (a <= 10)
    return 500000;
  else if (a <= 15)
    return 300000;
  else if (a <= 21)
    return 100000;
  else
    return 0;
}
int festival2(int a) {
  if (a == 0)
    return 0;
  else if (a == 1)
    return 5120000;
  else if (a <= 3)
    return 2560000;
  else if (a <= 7)
    return 1280000;
  else if (a <= 15)
    return 640000;
  else if (a <= 31)
    return 320000;
  else
    return 0;
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int T;
  cin >> T;
  while (T--) {
    int a, b;
    cin >> a >> b;
    cout << festival1(a) + festival2(b) << '\n';
  }
  return 0;
}