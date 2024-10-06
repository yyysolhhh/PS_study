#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int N;
  cin >> N;
  vector<int> beads;
  for (int i = 0; i < N; i++) {
    int num;
    cin >> num;
    beads.push_back(num);
  }
  sort(beads.begin(), beads.end());
  int ans = 0;
  for (int i = N - 1; i > 0; i--) {
    ans += beads[i] - beads[i - 1];
  }
  ans += beads[N - 1] - beads[0];
  cout << ans;
  return 0;
}