#include <bits/stdc++.h>
using namespace std;
int T, N, M, ans;
int binary_search(int n, int A[]) {
  int cnt = 0;
  int left = 0, right = N - 1;
  while (left <= right) {
    int mid = (left + right) / 2;
    if (A[mid] <= n) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return N - left;
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> T;
  for (int i = 0; i < T; i++) {
    cin >> N >> M;
    int A[N], B[M];
    ans = 0;
    for (int j = 0; j < N; j++) {
      cin >> A[j];
    }
    for (int j = 0; j < M; j++) {
      cin >> B[j];
    }
    sort(A, A + N);
    for (int i = 0; i < M; i++) {
      ans += binary_search(B[i], A);
    }
    cout << ans << '\n';
  }
  return 0;
}