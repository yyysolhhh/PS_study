#include <bits/stdc++.h>
using namespace std;
int get_gcd(int a, int b) {
  if (b == 0) return a;
  return get_gcd(b, a % b);
}

int get_lcm(int a, int b, int gcd) { return a * b / gcd; }

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int T;
  cin >> T;
  while (T--) {
    int a, b;
    cin >> a >> b;
    int gcd = get_gcd(a, b);
    cout << get_lcm(a, b, gcd) << ' ' << get_gcd(a, b) << '\n';
  }
  return 0;
}