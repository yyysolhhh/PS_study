#include <bits/stdc++.h>
using namespace std;
string pic[5];
void ready(int col) {
  string state = ".omln";
  for (int i = 0; i < 5; i++) {
    pic[i][col] = state[i];
  }
}
void jump(int col) {
  string state = "owln.";
  for (int i = 0; i < 5; i++) {
    pic[i][col] = state[i];
  }
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  for (int i = 0; i < 5; i++) {
    cin >> pic[i];
  }
  for (int i = 0; i < pic[0].length(); i++) {
    if (pic[1][i] == 'o') {
      jump(i);
    } else if (pic[1][i] == 'w') {
      ready(i);
    } else
      continue;
  }
  for (string s : pic) {
    cout << s << '\n';
  }
  return 0;
}