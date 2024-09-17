#include <iostream>
using namespace std;
int contain(int n) {
  while (n > 0) {
    if (n % 10 == 7) return 1;
    n /= 10;
  }
  return 0;
}
int is_divisible(int n) { return n % 7 == 0; }
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  cout << 2 * contain(n) + is_divisible(n);
  return 0;
}