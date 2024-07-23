#include <bits/stdc++.h>
using namespace std;
int N, M;
int board[101];
int visited[101];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> M;
  for (int i = 0; i < N + M; i++) {
    int x, y;
    cin >> x >> y;
    board[x] = y;
  }
  queue<int> Q;
  Q.push(1);
  visited[1] = 1;
  while (!Q.empty()) {
    int cur = Q.front();
    Q.pop();
    for (int i = 1; i <= 6; i++) {
      int next = cur + i;
      if (next < 1 || next > 100) continue;
      if (board[next] > 0) next = board[next];
      if (visited[next]) continue;
      visited[next] = visited[cur] + 1;
      Q.push(next);
    }
  }
  cout << visited[100] - 1;
  return 0;
}