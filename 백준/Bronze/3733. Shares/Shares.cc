#include <iostream>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, S, ans;
  while (cin >> N >> S) {
    ans = S / (N + 1);
    cout << ans << "\n";
  }
}