#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int N;
int visited[25][25];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N;
  char board[N][N];
  vector<int> res;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> board[i][j];
    }
  }
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (!visited[i][j] && board[i][j] == '1') {
        queue<pair<int, int>> Q;
        Q.push({i, j});
        visited[i][j] = 1;
        int area = 1;
        while (!Q.empty()) {
          auto cur = Q.front();
          Q.pop();
          for (int dir = 0; dir < 4; dir++) {
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];
            if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
            if (visited[nx][ny] || board[nx][ny] == '0') continue;
            visited[nx][ny] = 1;
            area++;
            Q.push({nx, ny});
          }
        }
        res.push_back(area);
      }
    }
  }
  sort(res.begin(), res.end());
  cout << res.size() << '\n';
  for (int area : res) {
    cout << area << '\n';
  }
}