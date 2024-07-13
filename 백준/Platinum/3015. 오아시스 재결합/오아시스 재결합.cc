#include <bits/stdc++.h>
#define H first
#define CNT second
using namespace std;
int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int N;
  cin >> N;
  long long res = 0;
  stack<pair<int, int>> st;
  for (int i = 0; i < N; i++) {
    int h;
    cin >> h;
    int cnt = 1;
    while (!st.empty() && h >= st.top().H) {
      res += st.top().CNT;
      if (h == st.top().H) {
        cnt += st.top().CNT;
      }
      st.pop();
    }
    if (!st.empty()) {
      res++;
    }
    st.push({h, cnt});
  }
  cout << res;
}