#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int T;
  ll sum;
  cin >> T;
  while (T--) {
    ll n;
    cin >> n;
    sum = 0;
    for (int i = 0; i < n; i++) {
      ll candy;
      cin >> candy;
      sum += candy % n;
    }
    if (sum % n)
      cout << "NO\n";
    else
      cout << "YES\n";
  }
  return 0;
}