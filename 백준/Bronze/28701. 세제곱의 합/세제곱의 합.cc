#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, ans1 = 0, ans2 = 0;
  cin >> N;
  for (int i = 1; i <= N; i++) {
    ans1 += i;
    ans2 += i * i * i;
  }
  cout << ans1 << '\n' << ans1 * ans1 << '\n' << ans2;
  return 0;
}