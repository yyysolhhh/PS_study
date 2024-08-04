#include <bits/stdc++.h>
using namespace std;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
string board[1001];
int visited[1001][1001][11];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, M, K;
  cin >> N >> M >> K;
  for (int i = 0; i < N; i++) {
    cin >> board[i];
  }
  queue<tuple<int, int, int>> Q;
  Q.push({0, 0, 0});
  visited[0][0][0] = 1;
  while (!Q.empty()) {
    auto cur = Q.front();
    Q.pop();
    int x, y, k;
    tie(x, y, k) = cur;
    if (x == N - 1 && y == M - 1) {
      cout << visited[x][y][k];
      return 0;
    }
    for (int dir = 0; dir < 4; dir++) {
      int nx = x + dx[dir];
      int ny = y + dy[dir];
      if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
      int nk = k;
      if (board[nx][ny] == '1') {
        nk++;
      }
      if (nk > K || visited[nx][ny][nk] > 0) continue;
      visited[nx][ny][nk] = visited[x][y][k] + 1;
      Q.push({nx, ny, nk});
    }
  }
  cout << -1;
  return 0;
}