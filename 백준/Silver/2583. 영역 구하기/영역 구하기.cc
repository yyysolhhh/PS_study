#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int board[100][100];
int visited[100][100];
vector<int> width;
int M, N, K;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> M >> N >> K;
  for (int i = 0; i < K; i++) {
    int lx, ly, rx, ry;
    cin >> lx >> ly >> rx >> ry;
    for (int x = ly; x < ry; x++) {
      for (int y = lx; y < rx; y++) {
        board[x][y] += 1;
      }
    }
  }
  for (int i = 0; i < M; i++) {
    for (int j = 0; j < N; j++) {
      if (!board[i][j] && !visited[i][j]) {
        int w = 1;
        queue<pair<int, int>> Q;
        Q.push({i, j});
        visited[i][j] = 1;
        while (!Q.empty()) {
          auto cur = Q.front();
          Q.pop();
          for (int dir = 0; dir < 4; dir++) {
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];
            if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;
            if (board[nx][ny] > 0 || visited[nx][ny] == 1) continue;
            visited[nx][ny] = 1;
            w++;
            Q.push({nx, ny});
          }
        }
        width.push_back(w);
      }
    }
  }
  cout << width.size() << '\n';
  sort(width.begin(), width.end());
  for (int w : width) {
    cout << w << ' ';
  }
}