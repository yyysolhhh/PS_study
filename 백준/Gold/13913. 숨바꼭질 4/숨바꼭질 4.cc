#include <bits/stdc++.h>
using namespace std;
int MAX = 200000;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, K;
  cin >> N >> K;
  int visited[MAX];
  int preLoc[MAX];
  fill(visited, visited + MAX, -1);
  fill(preLoc, preLoc + MAX, -1);
  queue<int> Q;
  Q.push(N);
  visited[N] = 0;
  while (!Q.empty()) {
    int cur = Q.front();
    Q.pop();
    for (int next : {cur - 1, cur + 1, 2 * cur}) {
      if (next < 0 || next >= MAX) continue;
      if (visited[next] >= 0) continue;
      visited[next] = visited[cur] + 1;
      Q.push(next);
      preLoc[next] = cur;
    }
  }
  cout << visited[K] << '\n';
  stack<int> st;
  st.push(K);
  while (st.top() != N) {
    st.push(preLoc[st.top()]);
  }
  while (!st.empty()) {
    cout << st.top() << ' ';
    st.pop();
  }
}