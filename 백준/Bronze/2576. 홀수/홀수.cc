#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int sum = 0, min = 101, n, i = 0;
  while (i < 7) {
    cin >> n;
    if (n & 1) {
      sum += n;
      if (n < min)
        min = n;
    }
    i++;
  }
  if (sum)
    cout << sum << '\n' << min;
  else
    cout << -1;
}