#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  string s;
  getline(cin, s);
  stack<char> st;
  int temp = 1;
  int res = 0;
  for (int i = 0; i < s.length(); i++) {
    if (s[i] == '(') {
      st.push('(');
      temp *= 2;
    } else if (s[i] == '[') {
      st.push('[');
      temp *= 3;
    } else if (s[i] == ')') {
      if (st.empty() || st.top() != '(') {
        cout << 0;
        return 0;
      }
      if (s[i - 1] == '(') {
        res += temp;
      }
      temp /= 2;
      st.pop();
    } else if (s[i] == ']') {
      if (st.empty() || st.top() != '[') {
        cout << 0;
        return 0;
      }
      if (s[i - 1] == '[') {
        res += temp;
      }
      temp /= 3;
      st.pop();
    }
  }
  if (!st.empty()) {
    cout << 0;
  } else {
    cout << res;
  }
}