#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  double p[10];
  for (int i = 0; i < 10; i++) {
    cin >> p[i];
  }
  sort(p, p + 10);
  double ans = 1;
  for (int i = 1; i < 10; i++) {
    ans *= p[i] / i;
  }
  cout << fixed;
  cout << ans * pow(10, 9);
  return 0;
}