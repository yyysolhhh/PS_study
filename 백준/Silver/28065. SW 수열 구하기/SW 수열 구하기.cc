#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  int num = 1;
  for (int i = 1; i <= N; i++) {
    cout << num << ' ';
    if (i % 2 == 1)
      num += N - i;
    else
      num -= N - i;
  }
  return 0;
}