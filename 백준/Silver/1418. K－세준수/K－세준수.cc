#include <bits/stdc++.h>
using namespace std;
int prime_factor[100001];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, K;
  cin >> N >> K;
  int ans = 0;
  for (int i = 2; i <= N; i++) {
    if (prime_factor[i]) continue;
    for (int j = 1; j * i <= N; j++) {
      prime_factor[i * j] = i;
    }
  }
  for (int i = 1; i <= N; i++) {
    if (prime_factor[i] <= K) ans++;
  }
  cout << ans;
  return 0;
}