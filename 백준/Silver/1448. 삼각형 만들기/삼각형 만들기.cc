#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  int ans = -1;
  int straws[N];
  for (int i = 0; i < N; i++) {
    cin >> straws[i];
  }
  sort(straws, straws + N);
  while (N >= 3) {
    if (straws[N - 1] < straws[N - 2] + straws[N - 3]) {
      ans = straws[N - 1] + straws[N - 2] + straws[N - 3];
      break;
    }
    N--;
  }
  cout << ans;
  return 0;
}