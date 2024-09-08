#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int dx[2] = {1, 0};
int dy[2] = {0, 1};
int board[4][4];
int visited[4][4];
int N;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> board[i][j];
    }
  }
  queue<pair<int, int>> Q;
  Q.push({0, 0});
  visited[0][0] = 1;
  while (!Q.empty()) {
    auto cur = Q.front();
    Q.pop();
    for (int i = 0; i < 2; i++) {
      int nx = cur.X + board[cur.X][cur.Y] * dx[i];
      int ny = cur.Y + board[cur.X][cur.Y] * dy[i];
      if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
      if (visited[nx][ny] == 1) continue;
      visited[nx][ny] = 1;
      Q.push({nx, ny});
    }
  }
  if (visited[N - 1][N - 1] == 1)
    cout << "HaruHaru";
  else
    cout << "Hing";
  return 0;
}