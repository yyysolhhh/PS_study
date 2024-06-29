#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  string brackets;
  getline(cin, brackets);
  stack<char> st;
  int res = 0;
  for (int i = 0; i < brackets.length(); i++) {
    if (brackets[i] == '(') {
      st.push(brackets[i]);
    } else if (brackets[i] == ')') {
      if (brackets[i - 1] == ')') {
        st.pop();
        res++;
      } else {
        st.pop();
        res += st.size();
      }
    }
  }
  cout << res;
}