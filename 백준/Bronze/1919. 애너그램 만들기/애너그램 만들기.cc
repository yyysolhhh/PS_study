#include <bits/stdc++.h>
using namespace std;

int cnt[26];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  string s1, s2;
  cin >> s1 >> s2;

  int res = 0;
  for (auto c : s1)
    cnt[c - 'a']++;
  for (auto c : s2)
    cnt[c - 'a']--;
  for (int i = 0; i < 26; i++)
    res += abs(cnt[i]);
  cout << res;
}