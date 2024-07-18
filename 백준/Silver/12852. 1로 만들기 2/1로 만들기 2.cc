#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  int D[N + 1];
  int preLoc[N + 1];
  D[1] = 0;
  for (int i = 2; i <= N; i++) {
    D[i] = D[i - 1] + 1;
    preLoc[i] = i - 1;
    if (i % 3 == 0 && D[i] > D[i / 3] + 1) {
      D[i] = D[i / 3] + 1;
      preLoc[i] = i / 3;
    }
    if (i % 2 == 0 && D[i] > D[i / 2] + 1) {
      D[i] = D[i / 2] + 1;
      preLoc[i] = i / 2;
    }
  }
  cout << D[N] << '\n';
  int next = N;
  while (true) {
    cout << next << ' ';
    if (next == 1) break;
    next = preLoc[next];
  }
  return 0;
}