#include <bits/stdc++.h>
using namespace std;
char board[101][101];
void print_result(char c) {
  switch (c) {
    case '-':
      cout << '|';
      break;
    case '|':
      cout << '-';
      break;
    case '/':
      cout << '\\';
      break;
    case '\\':
      cout << '/';
      break;
    case '^':
      cout << '<';
      break;
    case '<':
      cout << 'v';
      break;
    case 'v':
      cout << '>';
      break;
    case '>':
      cout << '^';
      break;
    default:
      cout << c;
      break;
  }
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, M;
  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      cin >> board[i][j];
    }
  }
  for (int i = M - 1; i >= 0; i--) {
    for (int j = 0; j < N; j++) {
      print_result(board[j][i]);
    }
    cout << '\n';
  }
  return 0;
}