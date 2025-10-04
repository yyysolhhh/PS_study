#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
const int INF = 0x3f3f3f3f;
int n, m;
vector<pair<int, int>> adj[1001];
int d[1001];
int pre[1001];
void dijstra(int start) {
  priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
  pq.push({0, start});
  d[start] = 0;
  pre[start] = 0;
  while (!pq.empty()) {
    auto cur = pq.top(); pq.pop();
    if (d[cur.Y] != cur.X) continue;
    for (auto nxt: adj[cur.Y]) {
      if (d[nxt.Y] <= d[cur.Y] + nxt.X) continue;
      d[nxt.Y] = d[cur.Y] + nxt.X;
      pq.push({d[nxt.Y], nxt.Y});
      pre[nxt.Y] = cur.Y;
    }
  }
}
void find_path(int start, int end) {
  int idx = end;
  deque<int> path;
  path.push_front(end);
  while (idx != start) {
    path.push_front(pre[idx]);
    idx = pre[idx];
  }
  cout << path.size() << "\n";
  for (auto x : path) {
    cout << x << " ";
  }
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 1; i <= m; i++) {
    int s, e, w;
    cin >> s >> e >> w;
    adj[s].push_back({w, e});
  }
  int start, end;
  cin >> start >> end;
  fill(d, d + n + 1, INF);
  dijstra(start);
  cout << d[end] << "\n";
  find_path(start, end);
  return 0;
}