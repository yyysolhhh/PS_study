#include <bits/stdc++.h>
using namespace std;
using ll = long long;
ll colors[2][10001];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  ll X, K;
  cin >> X >> K;
  ll color;
  ll ans;
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < X; j++) {
      cin >> color;
      colors[i][color]++;
    }
  }
  ans = X * X;
  for (int i = 1; i <= K; i++) {
    if (colors[0][i] > 0 && colors[1][i] > 0) {
      ans -= colors[0][i] * colors[1][i];
    }
  }
  cout << ans;
  return 0;
}