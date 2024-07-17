#include <bits/stdc++.h>
using namespace std;
int stair;
int point[301];
int dp[301][3];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> stair;
  for (int i = 1; i <= stair; i++) {
    cin >> point[i];
  }
  dp[1][1] = point[1];
  dp[1][2] = point[1];
  for (int i = 2; i <= stair; i++) {
    dp[i][1] = point[i] + max(dp[i - 2][1], dp[i - 2][2]);
    dp[i][2] = point[i] + dp[i - 1][1];
  }
  cout << max(dp[stair][1], dp[stair][2]);
  return 0;
}