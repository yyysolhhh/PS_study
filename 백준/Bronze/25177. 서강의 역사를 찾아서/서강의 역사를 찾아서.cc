#include <bits/stdc++.h>
using namespace std;
int now[1001];
int before[1001];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, M;
  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    cin >> now[i];
  }
  for (int i = 0; i < M; i++) {
    cin >> before[i];
  }
  int ans = 0;
  for (int i = 0; i < M; i++) {
    ans = max(ans, before[i] - now[i]);
  }
  cout << ans;
  return 0;
}