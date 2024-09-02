#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int A, B, C, D;
  cin >> A >> B >> C >> D;
  A = (A + (B + (C + D) / 60) / 60) % 24;
  B = (B + (C + D) / 60) % 60;
  C = (C + D) % 60;
  cout << A << ' ' << B << ' ' << C;
  return 0;
}