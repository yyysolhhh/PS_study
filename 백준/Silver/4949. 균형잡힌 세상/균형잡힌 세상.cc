#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  while (true) {
    string s;
    getline(cin, s);
    if (s == ".")
      break;
    stack<char> St;
    string res = "yes";
    int i = 0;
    while (s[i] != '.') {
      if (s[i] == '(' || s[i] == '[') {
        St.push(s[i]);
      } else if (s[i] == ')') {
        if (St.empty() || St.top() != '(') {
          res = "no";
          break;
        } else
          St.pop();
      } else if (s[i] == ']') {
        if (St.empty() || St.top() != '[') {
          res = "no";
          break;
        } else
          St.pop();
      }
      i++;
    }
    if (!St.empty())
      res = "no";
    cout << res << '\n';
  }
}