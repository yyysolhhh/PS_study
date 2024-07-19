#include <bits/stdc++.h>
using namespace std;
int dx[12] = {1, -1, 0, 0, -2, -1, -2, -1, 2, 1, 2, 1};
int dy[12] = {0, 0, 1, -1, 1, 2, -1, -2, 1, 2, -1, -2};
int board[201][201];
int dist[31][201][201];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int K, W, H;
  cin >> K >> W >> H;
  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      cin >> board[i][j];
    }
  }
  queue<tuple<int, int, int>> Q;
  dist[0][0][0] = 1;
  Q.push({0, 0, 0});
  while (!Q.empty()) {
    int k, x, y;
    tie(k, x, y) = Q.front();
    Q.pop();
    if (k < K) {
      for (int dir = 4; dir < 12; dir++) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        if (nx < 0 || nx >= H || ny < 0 || ny >= W) continue;
        if (board[nx][ny] == 1 || dist[k + 1][nx][ny]) continue;
        dist[k + 1][nx][ny] = dist[k][x][y] + 1;
        Q.push({k + 1, nx, ny});
      }
    }
    for (int dir = 0; dir < 4; dir++) {
      int nx = x + dx[dir];
      int ny = y + dy[dir];
      if (nx < 0 || nx >= H || ny < 0 || ny >= W) continue;
      if (board[nx][ny] == 1 || dist[k][nx][ny]) continue;
      dist[k][nx][ny] = dist[k][x][y] + 1;
      Q.push({k, nx, ny});
    }
  }
  int ans = 2147483647;
  for (int i = 0; i <= K; i++) {
    if (dist[i][H - 1][W - 1]) ans = min(ans, dist[i][H - 1][W - 1]);
  }
  if (ans == 2147483647)
    cout << -1;
  else
    cout << ans - 1;
  return 0;
}