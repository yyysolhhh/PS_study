#include <bits/stdc++.h>
using namespace std;
int T;
int dp[11];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> T;
  while (T--) {
    int n;
    cin >> n;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    for (int i = 4; i <= n; i++) {
      dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }
    cout << dp[n] << '\n';
  }
  return 0;
}