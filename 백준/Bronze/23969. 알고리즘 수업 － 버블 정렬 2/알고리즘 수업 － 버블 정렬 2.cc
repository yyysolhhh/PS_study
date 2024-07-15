#include <bits/stdc++.h>
using namespace std;
int N, K;

int bubble_sort(int *A) {
  int k = 0;
  for (int i = N - 1; i > 0; i--) {
    for (int j = 0; j < i; j++) {
      if (A[j] > A[j + 1]) {
        int temp;
        temp = A[j];
        A[j] = A[j + 1];
        A[j + 1] = temp;
        k++;
      }
      if (k == K) return k;
    }
  }
  return -1;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> K;
  int A[N];
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  int k = bubble_sort(A);
  if (k == -1) {
    cout << -1;
  } else {
    for (int i = 0; i < N; i++) {
      cout << A[i] << ' ';
    }
  }
  return 0;
}