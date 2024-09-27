#include <bits/stdc++.h>
using namespace std;
vector<int> v;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, P;
  while (true) {
    cin >> N;
    if (N == 0) break;
    cin >> P;
    if (P % 2 == 1)
      v = {P + 1, N - P, N - P + 1};
    else
      v = {P - 1, N - P + 1, N - P + 2};
    sort(v.begin(), v.end());
    for (int i = 0; i < v.size(); i++) {
      cout << v[i] << ' ';
    }
  }
  return 0;
}