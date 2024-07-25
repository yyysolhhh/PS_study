#include <bits/stdc++.h>
using namespace std;
deque<int> dq;
void operate() {
  int temp;
  temp = dq.front();
  dq.pop_front();
  dq.push_back(temp);
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, M;
  cin >> N >> M;
  int ans = 0;
  for (int i = 1; i <= N; i++) {
    dq.push_back(i);
  }
  while (M--) {
    int pos;
    cin >> pos;
    int cnt = 0;
    int len = dq.size();
    while (true) {
      if (dq.front() == pos) {
        dq.pop_front();
        break;
      }
      operate();
      cnt++;
    }
    if (cnt <= len / 2) {
      ans += cnt;
    } else {
      ans += len - cnt;
    }
  }
  cout << ans;
  return 0;
}