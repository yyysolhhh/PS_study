#include <bits/stdc++.h>
using namespace std;
vector<int> A(10000);
int N, M, ans;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  int left = 0, right = 0;
  while (left < N && right < N) {
    int sum = accumulate(A.begin() + left, A.begin() + right + 1, 0);
    if (sum == M) {
      left++;
      right++;
      ans++;
    } else if (sum < M) {
      right++;
    } else {
      left++;
    }
  }
  cout << ans;
  return 0;
}