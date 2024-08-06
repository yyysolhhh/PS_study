#include <bits/stdc++.h>
using namespace std;
int order;
void solve(int size, int r, int c) {
  if (size == 1) return;
  if (r < size / 2 && c < size / 2) {
    solve(size / 2, r, c);
  } else if (r < size / 2 && c >= size / 2) {
    order += size / 2 * size / 2;
    solve(size / 2, r, c - size / 2);
  } else if (r >= size / 2 && c < size / 2) {
    order += size / 2 * size / 2 * 2;
    solve(size / 2, r - size / 2, c);
  } else {
    order += size / 2 * size / 2 * 3;
    solve(size / 2, r - size / 2, c - size / 2);
  }
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, r, c;
  cin >> N >> r >> c;
  int size = pow(2, N);
  solve(size, r, c);
  cout << order << '\n';
  return 0;
}