#include <iostream>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, ans;
  while (true) {
    cin >> n;
    if (n == 0) break;
    ans = 0;
    for (int i = 1; i <= n; i++) {
      ans += i;
    }
    cout << ans << '\n';
  }
  return 0;
}