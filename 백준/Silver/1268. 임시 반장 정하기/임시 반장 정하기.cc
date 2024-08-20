#include <bits/stdc++.h>
using namespace std;
int students[1001][5];
int cnt[1001];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    for (int j = 0; j < 5; j++) {
      cin >> students[i][j];
    }
  }
  for (int j = 1; j <= n; j++) {
    for (int k = 1; k <= n; k++) {
      for (int i = 0; i < 5; i++) {
        if (students[j][i] == students[k][i]) {
          cnt[j]++;
          break;
        }
      }
    }
  }
  int max_std = 0;
  int ans = 1;
  for (int i = 1; i <= n; i++) {
    if (cnt[i] > max_std) {
      max_std = cnt[i];
      ans = i;
    }
  }
  cout << ans;
  return 0;
}