#include <bits/stdc++.h>
using namespace std;

int N;
int dp[17], T[17], P[17];
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N;
  for (int i = 1; i <= N; i++) {
    cin >> T[i] >> P[i];
  }
  for (int i = 1; i <= N; i++) {
    dp[i] = max(dp[i], dp[i - 1]);
    if (i + T[i] - 1 <= N) dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i]);
  }
  cout << max(dp[N], dp[N + 1]);
  return 0;
}