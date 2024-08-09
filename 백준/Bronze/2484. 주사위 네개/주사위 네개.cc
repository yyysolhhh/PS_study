#include <bits/stdc++.h>
using namespace std;
int die[7];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  int ans = 0;
  for (int i = 0; i < N; i++) {
    fill(die, die + 7, 0);
    for (int j = 0; j < 4; j++) {
      int k;
      cin >> k;
      die[k] += 1;
    }
    int prize = 0;
    for (int i = 1; i <= 6; i++) {
      if (die[i] == 4) {
        prize = 50000 + i * 5000;
        break;
      } else if (die[i] == 3) {
        prize = 10000 + i * 1000;
        break;
      } else if (die[i] == 2) {
        prize = 1000 + i * 100;
        for (int j = i + 1; j <= 6; j++) {
          if (die[j] == 2) {
            prize = 2000 + i * 500 + j * 500;
            break;
          }
        }
        break;
      } else if (die[i] == 1) {
        prize = i * 100;
      }
    }
    ans = max(ans, prize);
  }
  cout << ans;
  return 0;
}