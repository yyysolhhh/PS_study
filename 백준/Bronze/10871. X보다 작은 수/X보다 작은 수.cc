#include <bits/stdc++.h>
using namespace std;

int main(void) {
  int N, X;
  cin >> N >> X;

  int A[N];
  for (int i = 0; i < N; i++) {
    scanf("%d", &A[i]);
  }
  for (int i = 0; i < N; i++) {
    if (A[i] < X)
      cout << A[i] << " ";
  }
}