#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int R, C;
string board[1000];
int visF[1000][1000];
int visJ[1000][1000];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> R >> C;
  queue<pair<int, int>> fireQ;
  queue<pair<int, int>> jQ;
  for (int i = 0; i < R; i++) {
    cin >> board[i];
    fill(visF[i], visF[i] + C, -1);
    fill(visJ[i], visJ[i] + C, -1);
    for (int j = 0; j < C; j++) {
      if (board[i][j] == 'F') {
        fireQ.push({i, j});
        visF[i][j] = 0;
      } else if (board[i][j] == 'J') {
        jQ.push({i, j});
        visJ[i][j] = 0;
      }
    }
  }
  while (!fireQ.empty()) {
    auto cur = fireQ.front();
    fireQ.pop();
    for (int i = 0; i < 4; i++) {
      int nx = cur.X + dx[i];
      int ny = cur.Y + dy[i];
      if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
      if (board[nx][ny] == '#' || visF[nx][ny] >= 0) continue;
      visF[nx][ny] = visF[cur.X][cur.Y] + 1;
      fireQ.push({nx, ny});
    }
  }
  while (!jQ.empty()) {
    auto cur = jQ.front();
    jQ.pop();
    for (int i = 0; i < 4; i++) {
      int nx = cur.X + dx[i];
      int ny = cur.Y + dy[i];
      if (nx < 0 || nx >= R || ny < 0 || ny >= C) {
        cout << visJ[cur.X][cur.Y] + 1;
        return 0;
      }
      if (board[nx][ny] == '#' || visJ[nx][ny] >= 0) continue;
      if (visF[nx][ny] != -1 && visF[nx][ny] <= visJ[cur.X][cur.Y] + 1)
        continue;
      visJ[nx][ny] = visJ[cur.X][cur.Y] + 1;
      jQ.push({nx, ny});
    }
  }
  cout << "IMPOSSIBLE";
}