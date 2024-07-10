#include <bits/stdc++.h>
using namespace std;
int main(void) {
  int N;
  cin >> N;
  long long res = 0;
  stack<int> st;
  for (int i = 0; i < N; i++) {
    long long height;
    cin >> height;
    while (!st.empty() && height >= st.top()) {
      st.pop();
    }
    res += st.size();
    st.push(height);
  }
  cout << res;
}