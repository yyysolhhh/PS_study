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
      st.push(2);
      temp *= 2;
    } else if (s[i] == '[') {
      st.push(3);
      temp *= 3;
    } else if (s[i] == ')' || s[i] == ']') {
      if (st.empty() || (s[i] == ')' && st.top() != 2) ||
          (s[i] == ']' && st.top() != 3)) {
        cout << 0;
        return 0;
      }
      if (s[i - 1] == '(' || s[i - 1] == '[') {
        res += temp;
      }
      temp /= st.top();
      st.pop();
    }
  }
  if (!st.empty()) {
    cout << 0;
  } else {
    cout << res;
  }
}