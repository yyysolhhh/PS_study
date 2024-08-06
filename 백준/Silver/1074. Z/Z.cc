#include <bits/stdc++.h>
using namespace std;

int solve(int n, int r, int c) {
  int half = pow(2, n - 1);
  if (n == 0) return 0;
  if (r < half && c < half) {
    return solve(n - 1, r, c);
  } else if (r < half && c >= half) {
    return solve(n - 1, r, c - half) + half * half;
  } else if (r >= half && c < half) {
    return solve(n - 1, r - half, c) + half * half * 2;
  } else {
    return solve(n - 1, r - half, c - half) + half * half * 3;
  }
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, r, c;
  cin >> N >> r >> c;
  cout << solve(N, r, c);
  return 0;
}