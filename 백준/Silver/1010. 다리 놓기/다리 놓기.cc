#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int T;
  cin >> T;
  while (T--) {
    int N, M;
    cin >> N >> M;
    long long ans = 1;
    int r = 1;
    for (int i = M; i > M - N; i--) {
      ans *= i;
      ans /= r;
      r++;
    }
    cout << ans << '\n';
  }
  return 0;
}