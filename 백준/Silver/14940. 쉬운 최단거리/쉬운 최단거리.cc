#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int MAX = 1000;
int n, m;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  int board[n][m];
  int dist[n][m];
  queue<pair<int, int>> Q;
  for (int i = 0; i < n; i++) {
    fill(dist[i], dist[i] + m, -1);
    for (int j = 0; j < m; j++) {
      cin >> board[i][j];
      if (board[i][j] == 2) {
        dist[i][j] = 0;
        Q.push({i, j});
      } else if (board[i][j] == 0) {
        dist[i][j] = 0;
      }
    }
  }
  while (!Q.empty()) {
    auto cur = Q.front();
    Q.pop();
    for (int i = 0; i < 4; i++) {
      int nx = cur.X + dx[i];
      int ny = cur.Y + dy[i];
      if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
        continue;
      }
      if (board[nx][ny] == 0 || dist[nx][ny] != -1) {
        continue;
      }
      dist[nx][ny] = dist[cur.X][cur.Y] + 1;
      Q.push({nx, ny});
    }
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cout << dist[i][j] << ' ';
    }
    cout << '\n';
  }
}