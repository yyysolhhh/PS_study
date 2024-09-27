#include <bits/stdc++.h>
using namespace std;
int N, cnt;
int queen[15];
bool visited[15];
int is_dup(int cur, int i) {
  for (int j = 0; j < cur; j++) {
    if (queen[j] == i || j == cur || abs(queen[j] - i) == abs(cur - j))
      return 1;
  }
  return 0;
}
void nqueen(int cur) {
  if (cur == N) {
    cnt++;
    return;
  }
  for (int i = 0; i < N; i++) {
    if (visited[i] || is_dup(cur, i)) continue;
    queen[cur] = i;
    visited[i] = true;
    nqueen(cur + 1);
    visited[i] = false;
  }
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N;
  nqueen(0);
  cout << cnt;
  return 0;
}