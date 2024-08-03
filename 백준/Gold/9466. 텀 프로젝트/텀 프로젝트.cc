#include <bits/stdc++.h>
using namespace std;
#define CYCLE -1
#define NOT_VISITED 0
int board[100001];
int visited[100001];

void findCycle(int n) {
  int cur = n;
  while (true) {
    visited[cur] = n;
    cur = board[cur];
    if (visited[cur] == n) {
      while (visited[cur] != CYCLE) {
        visited[cur] = CYCLE;
        cur = board[cur];
      }
      return;
    } else if (visited[cur] != NOT_VISITED) {
      return;
    }
  }
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int T;
  cin >> T;
  while (T--) {
    int num;
    cin >> num;
    fill(visited, visited + num + 1, NOT_VISITED);
    for (int i = 1; i <= num; i++) {
      cin >> board[i];
    }
    for (int i = 1; i <= num; i++) {
      if (visited[i] == NOT_VISITED) {
        findCycle(i);
      }
    }
    int ans = 0;
    for (int i = 1; i <= num; i++) {
      if (visited[i] != CYCLE) ans++;
    }
    cout << ans << '\n';
  }
  return 0;
}