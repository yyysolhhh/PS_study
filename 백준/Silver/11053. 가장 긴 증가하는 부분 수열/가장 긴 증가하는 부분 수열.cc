#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  int A[N];
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  int dp[N];
  int res = 0;
  fill(dp, dp + N, 1);
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < i; j++) {
      if (A[j] < A[i]) {
        dp[i] = max(dp[i], dp[j] + 1);
      }
    }
    res = max(res, dp[i]);
  }
  cout << res;
}