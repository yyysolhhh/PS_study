#include <bits/stdc++.h>
using namespace std;
int N, S;
int A[100005];
int ans = 0x7fffffff;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> S;
  for (int i = 0; i < N; i++) cin >> A[i];
  int en = 0, tot = A[0];
  for (int st = 0; st < N; st++) {
    while (en < N && tot < S) {
      en++;
      if (en != N)
        tot += A[en];
    }
    if (en == N) break;
    ans = min(ans, en - st + 1);
    tot -= A[st];
  }
  if (ans == 0x7fffffff) ans = 0;
  cout << ans;
  return 0;
}