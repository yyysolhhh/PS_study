#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  long long max_x = -100000, max_y = -100000, min_x = 100000, min_y = 100000;
  long long ans;
  cin >> N;
  while (N--) {
    long long x, y;
    cin >> x >> y;
    max_x = max(max_x, x);
    min_x = min(min_x, x);
    max_y = max(max_y, y);
    min_y = min(min_y, y);
  }
  ans = (max_x - min_x) * (max_y - min_y);
  cout << ans;
  return 0;
}