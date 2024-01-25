#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  string s;
  cin >> s;
  int res[26];
  fill(res, res + 26, 0);
  for (auto c : s) {
    res[c - 'a']++;
  }
  for (int i = 0; i < 26; i++) {
    cout << res[i] << ' ';
  }
}