#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  while (true) {
    int n;
    cin >> n;
    if (n == -1) break;
    stack<int> S;
    int sum = 0;
    for (int i = n - 1; i > 0; i--) {
      if (n % i == 0) {
        sum += i;
        S.push(i);
      }
    }
    if (sum == n) {
      cout << n << " = ";
      while (!S.empty()) {
        if (S.size() == 1)
          cout << S.top() << "\n";
        else
          cout << S.top() << " + ";
        S.pop();
      }
    } else {
      cout << n << " is NOT perfect.\n";
    }
  }
  return 0;
}