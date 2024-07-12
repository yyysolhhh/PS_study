#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int N;
int board[100][100];
int visited[100][100];
int dist[100][100];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> board[i][j];
    }
  }
  // 섬 구분
  int num = 0;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (board[i][j] == 1 && !visited[i][j]) {
        num++;
        queue<pair<int, int>> Q;
        Q.push({i, j});
        board[i][j] = num;
        while (!Q.empty()) {
          auto cur = Q.front();
          Q.pop();
          for (int dir = 0; dir < 4; dir++) {
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];
            if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
            if (!board[nx][ny] || visited[nx][ny]) continue;
            board[nx][ny] = num;
            visited[nx][ny] = 1;
            Q.push({nx, ny});
          }
        }
      }
    }
  }
  // 다리 놓기
  int ans = 11111;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      for (int i = 0; i < N; i++) {
        fill(dist[i], dist[i] + N, -1);
      }
      if (!board[i][j]) continue;
      queue<pair<int, int>> Q;
      dist[i][j] = 0;
      Q.push({i, j});
      while (!Q.empty()) {
        auto cur = Q.front();
        Q.pop();
        for (int dir = 0; dir < 4; dir++) {
          int nx = cur.X + dx[dir];
          int ny = cur.Y + dy[dir];
          if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
          if (dist[nx][ny] >= 0 || board[i][j] == board[nx][ny]) continue;
          if (board[nx][ny] && board[i][j] != board[nx][ny]) {
            ans = min(ans, dist[cur.X][cur.Y]);
            while (!Q.empty()) {
              Q.pop();
            }
            break;
          }
          dist[nx][ny] = dist[cur.X][cur.Y] + 1;
          Q.push({nx, ny});
        }
      }
    }
  }
  cout << ans;
}