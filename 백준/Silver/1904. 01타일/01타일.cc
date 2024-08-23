#include <bits/stdc++.h>
using namespace std;
int d[1000001];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  d[1] = 1;
  d[2] = 2;
  for (int i = 3; i <= N; i++) {
    d[i] = (d[i - 1] + d[i - 2]) % 15746;
  }
  cout << d[N];
  return 0;
}