#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int board[1000][1000];
int visited[1000][1000];
int N, M;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> M >> N;
  queue<pair<int, int>> Q;
  for (int x = 0; x < N; x++) {
    for (int y = 0; y < M; y++) {
      cin >> board[x][y];
      if (board[x][y] == 1) {
        Q.push({x, y});
      }
      if (board[x][y] == 0) {
        visited[x][y] = -1;
      }
    }
  }
  while (!Q.empty()) {
    pair<int, int> cur = Q.front();
    Q.pop();
    for (int dir = 0; dir < 4; dir++) {
      int nx = cur.X + dx[dir];
      int ny = cur.Y + dy[dir];
      if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
        continue;
      }
      if (visited[nx][ny] != -1 || board[nx][ny] == -1 || board[nx][ny] == 1) {
        continue;
      }
      visited[nx][ny] = visited[cur.X][cur.Y] + 1;
      Q.push({nx, ny});
    }
  }
  int res = 0;
  for (int x = 0; x < N; x++) {
    for (int y = 0; y < M; y++) {
      if (visited[x][y] == -1) {
        cout << -1;
        return 0;
      }
      res = max(res, visited[x][y]);
    }
  }
  cout << res;
}