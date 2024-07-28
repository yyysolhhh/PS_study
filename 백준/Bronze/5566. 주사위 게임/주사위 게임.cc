#include <bits/stdc++.h>
using namespace std;
int board[1001];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, M;
  cin >> N >> M;
  for (int i = 1; i <= N; i++) {
    cin >> board[i];
  }
  int cur = 1;
  for (int i = 1; i <= M; i++) {
    int num;
    cin >> num;
    cur += num;
    cur += board[cur];
    if (cur >= N) {
      cout << i;
      break;
    }
  }
  return 0;
}