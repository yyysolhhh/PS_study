#include <bits/stdc++.h>
using namespace std;
int N, S;
int nums[21];
int cnt;
void backtracking(int cur, int sum) {
  if (cur == N) {
    if (sum == S) {
      cnt++;
    }
    return;
  }
  backtracking(cur + 1, sum);
  backtracking(cur + 1, sum + nums[cur]);
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> S;
  for (int i = 0; i < N; i++) {
    cin >> nums[i];
  }
  backtracking(0, 0);
  if (S == 0) cnt--;
  cout << cnt;
  return 0;
}