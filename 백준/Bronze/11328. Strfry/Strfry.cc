#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n;
  cin >> n;
  while (n--) {
    int cnt[26] = {};
    string s1, s2;
    cin >> s1 >> s2;
    for (auto c : s1) {
      cnt[c - 'a']++;
    }
    for (auto c : s2) {
      cnt[c - 'a']--;
    }
    int is_possible = 1;
    for (auto n : cnt) {
      if (n != 0) {
        is_possible = 0;
        break;
      }
    }
    if (is_possible)
      cout << "Possible\n";
    else
      cout << "Impossible\n";
  }
}