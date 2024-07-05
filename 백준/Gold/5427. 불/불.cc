#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int t, w, h;
  cin >> t;
  while (t--) {
    cin >> w >> h;
    string board[h];
    int fire[h][w];
    int sang[h][w];
    bool isEscape = false;
    queue<pair<int, int> > fireQ;
    queue<pair<int, int> > sangQ;
    for (int i = 0; i < h; i++) {
      fill(fire[i], fire[i] + w, -1);
      fill(sang[i], sang[i] + w, -1);
    }
    for (int i = 0; i < h; i++) {
      cin >> board[i];
      for (int j = 0; j < w; j++) {
        if (board[i][j] == '@') {
          sangQ.push({i, j});
          sang[i][j] = 0;
        } else if (board[i][j] == '*') {
          fireQ.push({i, j});
          fire[i][j] = 0;
        }
      }
    }
    while (!fireQ.empty()) {
      auto cur = fireQ.front();
      fireQ.pop();
      for (int dir = 0; dir < 4; dir++) {
        int nx = cur.X + dx[dir];
        int ny = cur.Y + dy[dir];
        if (nx < 0 || nx >= h || ny < 0 || ny >= w) {
          continue;
        }
        if (board[nx][ny] == '#' || fire[nx][ny] >= 0) continue;
        fire[nx][ny] = fire[cur.X][cur.Y] + 1;
        fireQ.push({nx, ny});
      }
    }
    while (!sangQ.empty() && !isEscape) {
      auto cur = sangQ.front();
      sangQ.pop();
      for (int dir = 0; dir < 4; dir++) {
        int nx = cur.X + dx[dir];
        int ny = cur.Y + dy[dir];
        if (nx < 0 || nx >= h || ny < 0 || ny >= w) {
          cout << sang[cur.X][cur.Y] + 1 << '\n';
          isEscape = true;
          break;
        }
        if (board[nx][ny] == '#' || sang[nx][ny] >= 0) continue;
        if (fire[nx][ny] != -1 && fire[nx][ny] <= sang[cur.X][cur.Y] + 1)
          continue;
        sang[nx][ny] = sang[cur.X][cur.Y] + 1;
        sangQ.push({nx, ny});
      }
    }
    if (!isEscape) cout << "IMPOSSIBLE\n";
  }
  return 0;
}