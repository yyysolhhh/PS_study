#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  string S;
  cin >> N >> S;
  int cnt = 0;
  for (int i = 0; i < N; i++) {
    if (S[i] == 'J' || S[i] == 'A' || S[i] == 'V') {
      cnt++;
      continue;
    }
    cout << S[i];
  }
  if (cnt == S.length()) cout << "nojava";
  return 0;
}