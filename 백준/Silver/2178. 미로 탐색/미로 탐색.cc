#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
string board[100];
int dist[100][100];
int N, M;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> M;
  for (int x = 0; x < N; x++) {
    cin >> board[x];
  }
  queue<pair<int, int>> Q;
  Q.push({0, 0});
  dist[0][0] = 1;
  while (!Q.empty()) {
    pair<int, int> cur = Q.front();
    Q.pop();
    for (int dir = 0; dir < 4; dir++) {
      int nx = cur.X + dx[dir];
      int ny = cur.Y + dy[dir];
      if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
        continue;
      }
      if (dist[nx][ny] > 0 || board[nx][ny] != '1') {
        continue;
      }
      dist[nx][ny] = dist[cur.X][cur.Y] + 1;
      Q.push({nx, ny});
    }
  }
  cout << dist[N - 1][M - 1];
}