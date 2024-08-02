#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int N;
  cin >> N;
  string res;
  res = (N % 2) ? "Goose" : "Duck";
  cout << res;
  return 0;
}