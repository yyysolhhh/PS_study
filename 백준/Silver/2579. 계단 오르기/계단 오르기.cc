#include <bits/stdc++.h>
using namespace std;
int stair;
int point[301];
int dp[301];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> stair;
  for (int i = 1; i <= stair; i++) {
    cin >> point[i];
  }
  dp[1] = point[1];
  dp[2] = point[1] + point[2];
  dp[3] = max(point[3] + point[2], point[3] + point[1]);
  for (int i = 4; i <= stair; i++) {
    dp[i] = max(point[i] + point[i - 1] + dp[i - 3], point[i] + dp[i - 2]);
  }
  cout << dp[stair];
}