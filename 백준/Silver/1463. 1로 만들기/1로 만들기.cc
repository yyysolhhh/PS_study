#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  int D[N + 1];
  fill(D, D + N + 1, 0);
  for (int i = 2; i <= N; i++) {
    D[i] = D[i - 1] + 1;
    if (i % 3 == 0) {
      D[i] = min(D[i], D[i / 3] + 1);
    }
    if (i % 2 == 0) {
      D[i] = min(D[i], D[i / 2] + 1);
    }
  }
  cout << D[N];
}