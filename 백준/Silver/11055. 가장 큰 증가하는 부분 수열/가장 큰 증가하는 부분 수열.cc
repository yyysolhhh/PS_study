#include <bits/stdc++.h>
using namespace std;
int D[1001];
int A[1001];
int N;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> A[i];
    D[i] = A[i];
  }
  for (int i = 1; i < N; i++) {
    for (int j = i - 1; j >= 0; j--) {
      if (A[i] > A[j]) {
        D[i] = max(D[i], D[j] + A[i]);
      }
    }
  }
  cout << *max_element(D, D + N);
  return 0;
}