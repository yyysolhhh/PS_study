#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  int count[N];
  fill(count, count + N, -1);
  queue<int> Q;
  Q.push(N);
  count[N] = 0;
  while (!Q.empty()) {
    double cur = Q.front();
    Q.pop();
    for (double next : {cur / 3, cur / 2, cur - 1}) {
      if (next - int(next) != 0) continue;
      if (count[int(next)] >= 0) continue;
      count[int(next)] = count[int(cur)] + 1;
      Q.push(next);
    }
  }
  cout << count[1] << '\n';
}