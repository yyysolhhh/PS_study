#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  char c;
  string str;
  int cnt;
  while (true) {
    cin >> c;
    if (c == '#') break;
    getline(cin, str);
    cnt = 0;
    for (char s : str) {
      s = tolower(s);
      if (s == c) cnt++;
    }
    cout << c << ' ' << cnt << '\n';
  }
  return 0;
}