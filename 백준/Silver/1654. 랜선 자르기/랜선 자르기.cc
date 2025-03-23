#include <bits/stdc++.h>
using namespace std;
int K, N, lan[10001];
long binary_search() {
  long left = 1, right = *max_element(lan, lan + K);
  while (left <= right) {
    long mid = (left + right) / 2;
    int cnt = 0;
    for (int i = 0; i < K; i++) {
      cnt += lan[i] / mid;
    }
    if (cnt < N) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return right;
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> K >> N;
  for (int i = 0; i < K; i++) {
    cin >> lan[i];
  }
  cout << binary_search();
  return 0;
}