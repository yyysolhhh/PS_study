#include <bits/stdc++.h>
using namespace std;
int N, K;
int MX = 200000;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> K;
  int visited[MX];
  fill(visited, visited + MX, -1);
  deque<int> dq;
  visited[N] = 0;
  dq.push_back(N);
  while (!dq.empty()) {
    int cur = dq.front();
    dq.pop_front();
    if (cur * 2 < MX && visited[cur * 2] == -1) {
      visited[cur * 2] = visited[cur];
      dq.push_front(cur * 2);
    }
    for (int next : {cur - 1, cur + 1}) {
      if (next < 0 || next >= MX || visited[next] != -1) continue;
      visited[next] = visited[cur] + 1;
      dq.push_back(next);
    }
  }
  cout << visited[K];
}