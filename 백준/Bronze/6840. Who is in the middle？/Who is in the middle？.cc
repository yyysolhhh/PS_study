#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int bowls[3];
  for (int i = 0; i < 3; i++) {
    cin >> bowls[i];
  }
  sort(bowls, bowls + 3);
  cout << bowls[1];
  return 0;
}