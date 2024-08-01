#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int F, S, G, U, D;
  cin >> F >> S >> G >> U >> D;
  int visited[F + 1];
  fill(visited, visited + F + 1, -1);
  queue<int> Q;
  visited[S] = 0;
  Q.push(S);
  while (!Q.empty()) {
    int cur = Q.front();
    Q.pop();
    for (int next : {cur + U, cur - D}) {
      if (next > F || next < 1) continue;
      if (visited[next] >= 0) continue;
      visited[next] = visited[cur] + 1;
      Q.push(next);
    }
  }
  if (visited[G] != -1)
    cout << visited[G];
  else
    cout << "use the stairs";
  return 0;
}