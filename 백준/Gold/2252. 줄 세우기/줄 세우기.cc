#include <bits/stdc++.h>
using namespace std;
int N, M;
vector<int> adj[32001];
int deg[32001];
queue<int> q;
vector<int> result;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> N >> M;
  for (int i = 0; i < M; i++) {
    int A, B;
    cin >> A >> B;
    adj[A].push_back(B);
    deg[B]++;
  }
  for (int i = 1; i <= N; i++) {
    if (deg[i] == 0) q.push(i);
  }
  while (!q.empty()) {
    int cur = q.front(); q.pop();
    result.push_back(cur);
    for (int nxt: adj[cur]) {
      deg[nxt]--;
      if (deg[nxt] == 0) q.push(nxt);
    }
  }
  for (int x: result) cout << x << ' ';
  return 0;
}