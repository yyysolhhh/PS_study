#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  int res = 0;
  for (int i = 0; i < N; i++) {
    int C, K;
    cin >> C >> K;
    res += C * K;
  }
  cout << res;
  return 0;
}