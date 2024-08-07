#include <bits/stdc++.h>
using namespace std;
int N, M, K;
string board[1001];
int visited[1001][1001][11][2];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> M >> K;
  for (int i = 0; i < N; i++) {
    cin >> board[i];
  }
  queue<tuple<int, int, int, int>> Q;
  visited[0][0][0][0] = 1;
  Q.push({0, 0, 0, 0});
  while (!Q.empty()) {
    int x, y, k, t;
    tie(x, y, k, t) = Q.front();
    Q.pop();
    if (x == N - 1 && y == M - 1) {
      cout << visited[x][y][k][t];
      return 0;
    }
    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
      if (board[nx][ny] == '0') {
        int nk = k;
        int nt = 1 - t;
        if (visited[nx][ny][nk][nt] > 0) continue;
        visited[nx][ny][nk][nt] = visited[x][y][k][t] + 1;
        Q.push({nx, ny, nk, nt});
      } else {
        int nk = k;
        int nt = 1 - t;
        if (nt == 1) {
          nk++;
          if (nk > K || visited[nx][ny][nk][nt] > 0) continue;
          visited[nx][ny][nk][nt] = visited[x][y][k][t] + 1;
          Q.push({nx, ny, nk, nt});
        } else {
          if (visited[x][y][k][nt] > 0) continue;
          visited[x][y][k][nt] = visited[x][y][k][t] + 1;
          Q.push({x, y, k, nt});
        }
      }
    }
  }
  cout << -1;
  return 0;
}