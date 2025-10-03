#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int V, E, K;
vector<pair<int, int>> adj[20005];
const int INF = 1e9 + 10;
int d[20005];
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> V >> E >> K;
  fill(d, d + V + 1, INF);
  while (E--) {
    int u, v, w;
    cin >> u >> v >> w;
    adj[u].push_back({w, v});
  }
  priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
  d[K] = 0;
  pq.push({d[K], K});
  while (!pq.empty()) {
    auto cur = pq.top(); pq.pop();
    if (d[cur.Y] != cur.X) continue;
    for (auto nxt : adj[cur.Y]) {
      if (d[nxt.Y] <= d[cur.Y] + nxt.X) continue;
      d[nxt.Y] = d[cur.Y] + nxt.X;
      pq.push({d[nxt.Y], nxt.Y});
    }
  }
  for (int i = 1; i <= V; i++) {
    if (d[i] == INF) cout << "INF\n";
    else cout << d[i] << "\n";
  }
  return 0;
}