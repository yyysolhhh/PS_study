#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, M;
  cin >> N >> M;
  int sum[N + 1];
  sum[0] = 0;
  for (int i = 1; i <= N; i++) {
    int num;
    cin >> num;
    sum[i] = sum[i - 1] + num;
  }
  while (M--) {
    int i, j;
    cin >> i >> j;
    cout << sum[j] - sum[i - 1] << '\n';
  }
  return 0;
}