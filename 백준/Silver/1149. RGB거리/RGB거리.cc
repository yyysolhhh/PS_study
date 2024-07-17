#include <bits/stdc++.h>
using namespace std;
int D[1001][3];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  int board[N][3];
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < 3; j++) {
      cin >> board[i][j];
    }
  }
  D[0][0] = board[0][0];
  D[0][1] = board[0][1];
  D[0][2] = board[0][2];
  for (int i = 1; i < N; i++) {
    D[i][0] = board[i][0] + min(D[i - 1][1], D[i - 1][2]);
    D[i][1] = board[i][1] + min(D[i - 1][0], D[i - 1][2]);
    D[i][2] = board[i][2] + min(D[i - 1][0], D[i - 1][1]);
  }
  int ans = min(D[N - 1][0], D[N - 1][1]);
  ans = min(ans, D[N - 1][2]);
  cout << ans;
  return 0;
}