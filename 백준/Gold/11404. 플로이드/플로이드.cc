#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, m;
  cin >> n >> m;
  vector<vector<int>> cost(n + 1, vector<int>(n + 1, INF));
  for (int i = 0; i < m; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    cost[a][b] = min(cost[a][b], c);
  }
  for (int i = 1; i <= n; i++) cost[i][i] = 0;
  for (int k = 1; k <= n; k++) {
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j]);
      }
    }
  }
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      if (cost[i][j] == INF) cout << 0 << " ";
      else cout << cost[i][j] << " ";
    }
    cout << "\n";
  }
  return 0;
}