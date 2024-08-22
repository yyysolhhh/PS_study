#include <bits/stdc++.h>
using namespace std;
int dp[10001];
int quantity[10001];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> quantity[i];
  }
  dp[1] = quantity[1];
  dp[2] = quantity[1] + quantity[2];
  for (int i = 3; i <= n; i++) {
    dp[i] = max({dp[i - 1], dp[i - 2] + quantity[i],
                 dp[i - 3] + quantity[i - 1] + quantity[i]});
  }
  cout << dp[n];
  return 0;
}