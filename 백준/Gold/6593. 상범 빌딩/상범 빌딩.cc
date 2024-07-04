#include <bits/stdc++.h>
using namespace std;
char board[30][30][30];
int visited[30][30][30];
int dx[6] = {0, 0, 0, 0, 1, -1};
int dy[6] = {0, 0, -1, 1, 0, 0};
int dz[6] = {1, -1, 0, 0, 0, 0};
int L, R, C;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  while (true) {
    cin >> L >> R >> C;
    if (!L && !R && !C) {
      return 0;
    }
    bool isEscape = false;
    queue<tuple<int, int, int>> Q;
    for (int i = 0; i < L; i++) {
      for (int j = 0; j < R; j++) {
        for (int k = 0; k < C; k++) {
          cin >> board[i][j][k];
          visited[i][j][k] = 0;
          if (board[i][j][k] == 'S') {
            Q.push({i, j, k});
          } else if (board[i][j][k] == '.' || board[i][j][k] == 'E') {
            visited[i][j][k] = -1;
          }
        }
      }
    }
    while (!Q.empty()) {
      if (isEscape) {
        break;
      }
      auto cur = Q.front();
      Q.pop();
      int curZ = get<0>(cur);
      int curX = get<1>(cur);
      int curY = get<2>(cur);
      for (int i = 0; i < 6; i++) {
        int nz = curZ + dz[i];
        int nx = curX + dx[i];
        int ny = curY + dy[i];
        if (nz < 0 || nz >= L || nx < 0 || nx >= R || ny < 0 || ny >= C) {
          continue;
        }
        if (visited[nz][nx][ny] > -1 || board[nz][nx][ny] == '#') {
          continue;
        }
        visited[nz][nx][ny] = visited[curZ][curX][curY] + 1;
        if (board[nz][nx][ny] == 'E') {
          cout << "Escaped in " << visited[nz][nx][ny] << " minute(s).\n";
          isEscape = true;
          break;
        }
        Q.push({nz, nx, ny});
      }
    }
    while (!Q.empty()) {
      Q.pop();
    }
    if (!isEscape) {
      cout << "Trapped!\n";
    }
  }
}