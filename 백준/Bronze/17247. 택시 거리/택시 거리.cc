#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, M;
  cin >> N >> M;
  vector<pair<int, int>> loc;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      int taxi;
      cin >> taxi;
      if (taxi == 1) {
        loc.push_back({i, j});
      }
    }
  }
  cout << abs(loc[1].X - loc[0].X) + abs(loc[1].Y - loc[0].Y);
  return 0;
}