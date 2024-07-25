#include <bits/stdc++.h>
using namespace std;
#define I first
#define H second
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  while (true) {
    int n;
    cin >> n;
    if (!n) break;
    long long ans = 0;
    stack<pair<long long, long long>> st;
    for (int i = 0; i < n; i++) {
      int h;
      cin >> h;
      int idx = i;
      while (!st.empty() && st.top().H >= h) {
        ans = max(ans, (i - st.top().I) * st.top().H);
        idx = st.top().I;
        st.pop();
      }
      st.push({idx, h});
    }
    while (!st.empty()) {
      ans = max(ans, (n - st.top().I) * st.top().H);
      st.pop();
    }
    cout << ans << '\n';
  }
  return 0;
}