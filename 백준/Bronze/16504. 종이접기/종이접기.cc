#include <iostream>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  long long ans = 0;
  for (int i = 0; i < N * N; i++) {
    long long num;
    cin >> num;
    ans += num;
  }
  cout << ans;
  return 0;
}