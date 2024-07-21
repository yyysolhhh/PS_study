#include <bits/stdc++.h>
using namespace std;
int D[100001];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  int numbers[n];
  for (int i = 0; i < n; i++) {
    cin >> numbers[i];
  }
  D[0] = numbers[0];
  for (int i = 1; i < n; i++) {
    D[i] = max(0, D[i - 1]) + numbers[i];
  }
  cout << *max_element(D, D + n);
  return 0;
}