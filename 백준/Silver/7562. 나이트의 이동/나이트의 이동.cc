#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int dx[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int dy[8] = {1, 2, 2, 1, -1, -2, -2, -1};
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int l, cur_x, cur_y, dest_x, dest_y;
    cin >> l >> cur_x >> cur_y >> dest_x >> dest_y;
    int board[l][l];
    for (int i = 0; i < l; i++) {
      fill(board[i], board[i] + l, -1);
    }
    queue<pair<int, int>> Q;
    board[cur_x][cur_y] = 0;
    Q.push({cur_x, cur_y});
    while (!Q.empty()) {
      pair<int, int> cur = Q.front();
      Q.pop();
      for (int dir = 0; dir < 8; dir++) {
        int nx = cur.X + dx[dir];
        int ny = cur.Y + dy[dir];
        if (nx < 0 || nx >= l || ny < 0 || ny >= l) {
          continue;
        }
        if (board[nx][ny] >= 0) {
          continue;
        }
        board[nx][ny] = board[cur.X][cur.Y] + 1;
        Q.push({nx, ny});
      }
    }
    cout << board[dest_x][dest_y] << '\n';
  }
}