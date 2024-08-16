#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  while (true) {
    string str;
    getline(cin, str);
    if (str == "#") break;
    int cnt = 0;
    for (char c : str) {
      if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
          c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
        cnt++;
      }
    }
    cout << cnt << '\n';
  }
  return 0;
}