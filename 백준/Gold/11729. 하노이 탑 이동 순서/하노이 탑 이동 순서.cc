#include <bits/stdc++.h>
using namespace std;
void hanoi(int a, int b, int n) {
  if (n == 1) {
    cout << a << ' ' << b << '\n';
    return;
  }
  hanoi(a, 6 - a - b, n - 1);
  cout << a << ' ' << b << '\n';
  hanoi(6 - a - b, b, n - 1);
}
int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int N;
  cin >> N;
  cout << (1 << N) - 1 << '\n';
  hanoi(1, 3, N);
  return 0;
}