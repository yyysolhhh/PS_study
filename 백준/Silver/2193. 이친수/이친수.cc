#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  long long dp[N + 1][2];
  dp[1][0] = 0;
  dp[1][1] = 1;
  for (int i = 2; i <= N; i++) {
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1];
    dp[i][1] = dp[i - 1][0];
  }
  cout << dp[N][0] + dp[N][1];
  return 0;
}