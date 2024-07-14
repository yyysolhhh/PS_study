#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  cin.ignore();
  while (N--) {
    int ans = 0;
    string s;
    getline(cin, s);
    for (int i : s) {
      if (i != ' ') ans += i - 'A' + 1;
    }
    if (ans == 100)
      cout << "PERFECT LIFE\n";
    else
      cout << ans << "\n";
  }
  return 0;
}