#include <bits/stdc++.h>
using namespace std;
int n, m;
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
  if (p[v] < p[u])
    swap(u, v);
  if (p[u] == p[v])
    p[u]--;
  p[v] = u;
  return true;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    int s, a, b;
    cin >> s >> a >> b;
    if (s == 0) {
      uni(a, b);
    } else if (s == 1) {
      if (find(a) == find(b))
        cout << "YES\n";
      else
        cout << "NO\n";
    }
  }
  return 0;
}