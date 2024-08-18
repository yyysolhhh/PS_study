#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int T;
  cin >> T;
  while (T--) {
    int a, b;
    char comma;
    cin >> a >> comma >> b;
    cout << a + b << '\n';
  }
  return 0;
}