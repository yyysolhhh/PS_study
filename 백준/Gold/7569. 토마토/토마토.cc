#include <bits/stdc++.h>
using namespace std;
int M, N, H;
int box[100][100][100];
int dist[100][100][100];
int dx[6] = {0, 0, 0, 0, 1, -1};
int dy[6] = {0, 0, 1, -1, 0, 0};
int dh[6] = {1, -1, 0, 0, 0, 0};

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> M >> N >> H;
  queue<tuple<int, int, int>> Q;
  for (int h = 0; h < H; h++) {
    for (int x = 0; x < N; x++) {
      for (int y = 0; y < M; y++) {
        cin >> box[h][x][y];
        if (box[h][x][y] == 0) {
          dist[h][x][y] = -1;
        } else if (box[h][x][y] == 1) {
          Q.push({h, x, y});
        }
      }
    }
  }
  while (!Q.empty()) {
    auto cur = Q.front();
    Q.pop();
    int curH, curX, curY;
    tie(curH, curX, curY) = cur;
    for (int dir = 0; dir < 6; dir++) {
      int nh = curH + dh[dir];
      int nx = curX + dx[dir];
      int ny = curY + dy[dir];
      if (nh < 0 || nh >= H || nx < 0 || nx >= N || ny < 0 || ny >= M) {
        continue;
      }
      if (box[nh][nx][ny] == -1 || dist[nh][nx][ny] > -1) {
        continue;
      }
      dist[nh][nx][ny] = dist[curH][curX][curY] + 1;
      Q.push({nh, nx, ny});
    }
  }
  int res = 0;
  for (int h = 0; h < H; h++) {
    for (int x = 0; x < N; x++) {
      for (int y = 0; y < M; y++) {
        if (dist[h][x][y] == -1) {
          cout << -1;
          return 0;
        }
        res = max(res, dist[h][x][y]);
      }
    }
  }
  cout << res;
}