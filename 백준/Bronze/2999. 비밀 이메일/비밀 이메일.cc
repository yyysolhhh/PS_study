#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  string msg;
  getline(cin, msg);
  int N = msg.length();
  int R = 0, C = 0;
  for (int c = 2; c <= N; c++) {
    for (int r = 1; r <= c; r++) {
      if (r * c == N && r > R) {
        R = r, C = c;
      }
    }
  }
  char arr[R + 1][C + 1];
  int k = 0;
  for (int i = 0; i < C; i++) {
    for (int j = 0; j < R; j++) {
      if (k < N) arr[j][i] = msg[k++];
    }
  }
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      cout << arr[i][j];
    }
  }
  return 0;
}