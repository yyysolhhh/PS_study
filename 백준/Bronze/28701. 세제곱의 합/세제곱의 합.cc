#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  int ans = (1 + N) * N / 2;
  cout << ans << '\n';
  cout << int(pow(ans, 2)) << '\n';
  cout << int(pow(ans, 2)) << '\n';
  return 0;
}