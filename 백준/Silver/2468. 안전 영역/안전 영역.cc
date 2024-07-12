#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int N;
int board[100][100];
int visited[100][100];

void bfs(int x, int y, int h) {
  queue<pair<int, int>> Q;
  Q.push({x, y});
  visited[x][y] = 1;
  while (!Q.empty()) {
    auto cur = Q.front();
    Q.pop();
    for (int i = 0; i < 4; i++) {
      int nx = cur.X + dx[i];
      int ny = cur.Y + dy[i];
      if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
      if (visited[nx][ny] || board[nx][ny] <= h) continue;
      visited[nx][ny] = 1;
      Q.push({nx, ny});
    }
  }
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N;
  int res = 0;
  int max_h = 0;
  for (int i = 0; i < N; i++) {
    fill(visited[i], visited[i] + N, 0);
    for (int j = 0; j < N; j++) {
      cin >> board[i][j];
      max_h = max(max_h, board[i][j]);
    }
  }
  for (int h = 0; h <= max_h; h++) {
    int cnt = 0;
    for (int i = 0; i < N; i++) {
      fill(visited[i], visited[i] + N, 0);
    }
    for (int x = 0; x < N; x++) {
      for (int y = 0; y < N; y++) {
        if (!visited[x][y] && board[x][y] > h) {
          bfs(x, y, h);
          cnt++;
        }
      }
    }
    res = max(res, cnt);
  }
  cout << res;
}