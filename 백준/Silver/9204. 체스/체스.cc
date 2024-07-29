#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int dx[4] = {-1, 1, -1, 1};
int dy[4] = {1, 1, -1, -1};
pair<int, int> board[8][8];
int dist[8][8];

void printPath(pair<int, int> start, pair<int, int> end) {
  vector<pair<int, int>> path;
  for (pair<int, int> i = end; i != start; i = board[i.X][i.Y]) {
    path.push_back(i);
  }
  path.push_back(start);
  reverse(path.begin(), path.end());
  for (auto p : path) {
    cout << char(p.Y + 'A') << ' ' << 8 - p.X << ' ';
  }
  cout << '\n';
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int T;
  cin >> T;
  while (T--) {
    for (int i = 0; i < 8; i++) {
      fill(dist[i], dist[i] + 8, -1);
      // fill(board[i], board[i] + 8, ({-1, -1}));
    }
    int x1, x2;
    char y1, y2;
    cin >> y1 >> x1 >> y2 >> x2;
    y1 -= 'A';
    y2 -= 'A';
    x1 = 8 - x1;
    x2 = 8 - x2;
    queue<pair<int, int>> Q;
    dist[x1][y1] = 0;
    board[x1][y1] = {x1, y1};
    Q.push({x1, y1});
    while (!Q.empty()) {
      auto cur = Q.front();
      Q.pop();
      for (int i = 0; i < 4; i++) {
        int nx = cur.X;
        int ny = cur.Y;
        while (nx >= 0 && nx < 8 && ny >= 0 && ny < 8) {
          nx += dx[i];
          ny += dy[i];
          if (nx < 0 || nx >= 8 || ny < 0 || ny >= 8) continue;
          if (dist[nx][ny] >= 0) continue;
          dist[nx][ny] = dist[cur.X][cur.Y] + 1;
          board[nx][ny] = cur;
          Q.push({nx, ny});
        }
      }
    }
    if (dist[x2][y2] >= 0) {
      cout << dist[x2][y2] << ' ';
      printPath({x1, y1}, {x2, y2});
      cout << '\n';
    } else {
      cout << "Impossible\n";
    }
  }
  return 0;
}