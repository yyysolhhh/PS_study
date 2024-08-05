#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  vector<int> v;
  for (int i = 0; i < 5; i++) {
    int n;
    cin >> n;
    v.push_back(n);
  }
  sort(v.begin(), v.end());
  cout << accumulate(v.begin(), v.end(), 0) / 5 << '\n';
  cout << v[2];
  return 0;
}