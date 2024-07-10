#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int board[300][300];
int N, M;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> N >> M;
  queue<pair<int, int>> Q1;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      cin >> board[i][j];
    }
  }
  int year = 0;
  while (true) {
    int iceCnt[N][M];
    for (int i = 0; i < N; i++) {
      fill(iceCnt[i], iceCnt[i] + M, 0);
      for (int j = 0; j < M; j++) {
        if (board[i][j] > 0) {
          Q1.push({i, j});
        }
      }
    }
    while (!Q1.empty()) {
      auto cur = Q1.front();
      Q1.pop();
      int cnt = 0;
      for (int dir = 0; dir < 4; dir++) {
        int nx = cur.X + dx[dir];
        int ny = cur.Y + dy[dir];
        if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
        if (board[nx][ny] == 0) {
          cnt++;
        }
      }
      iceCnt[cur.X][cur.Y] = cnt;
    }
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (board[i][j] - iceCnt[i][j] >= 0) {
          board[i][j] -= iceCnt[i][j];
        } else {
          board[i][j] = 0;
        }
      }
    }
    int ice = 0;
    int visited[N][M];
    for (int i = 0; i < N; i++) {
      fill(visited[i], visited[i] + M, 0);
    }
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (!visited[i][j] && board[i][j]) {
          queue<pair<int, int>> Q2;
          Q2.push({i, j});
          visited[i][j] = 1;
          while (!Q2.empty()) {
            auto cur = Q2.front();
            Q2.pop();
            for (int dir = 0; dir < 4; dir++) {
              int nx = cur.X + dx[dir];
              int ny = cur.Y + dy[dir];
              if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
              if (visited[nx][ny] > 0 || board[nx][ny] == 0) continue;
              visited[nx][ny] = 1;
              Q2.push({nx, ny});
            }
          }
          ice++;
        }
      }
    }
    year++;
    if (ice >= 2) {
      cout << year;
      return 0;
    } else if (ice == 0) {
      cout << 0;
      return 0;
    }
  }
}