#include <bits/stdc++.h>
using namespace std;
int N, K;
int visited[100001];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> K;
  queue<int> Q;
  Q.push(N);
  while (!Q.empty()) {
    int cur = Q.front();
    Q.pop();
    if (cur == K) {
      cout << visited[cur];
      return 0;
    }
    for (int next : {cur - 1, cur + 1, cur * 2}) {
      if (next < 0 || next > 100000 || visited[next]) continue;
      visited[next] = visited[cur] + 1;
      Q.push(next);
    }
  }
}