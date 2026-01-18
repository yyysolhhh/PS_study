#include <bits/stdc++.h>
using namespace std;
vector<int> p(1000001, -1);

int find(int x) {
  if (p[x] < 0)
    return x;
  return p[x] = find(p[x]);
}

bool uni(int u, int v) {
  u = find(u);
  v = find(v);
  if (u == v)
    return false;
  if (p[u] > p[v])
    swap(u, v);
  if (p[u] == p[v])
    p[u]--;
  p[v] = u;
  return true;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    cout << "Scenario " << i << ":\n";
    int n, k;
    cin >> n >> k;
    fill(p.begin(), p.begin() + n, -1);
    for (int j = 0; j < k; j++) {
      int a, b;
      cin >> a >> b;
      uni(a, b);
    }
    int m;
    cin >> m;
    for (int j = 0; j < m; j++) {
      int u, v;
      cin >> u >> v;
      cout << (find(u) == find(v)) << "\n";
    }
    cout << "\n";
  }
  return 0;
}