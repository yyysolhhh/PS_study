#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int sum = 0;
  int dw[9];
  for (int i = 0; i < 9; i++) {
    cin >> dw[i];
    sum += dw[i];
  }
  int extra = sum - 100;
  for (int i = 0; i < 9; i++) {
    for (int j = i + 1; j < 9; j++) {
      if (dw[i] + dw[j] == extra) {
        for (int k = 0; k < 9; k++) {
          if (k == i || k == j) continue;
          cout << dw[k] << '\n';
        }
        break;
      }
    }
  }
  return 0;
}