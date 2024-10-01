#include <bits/stdc++.h>
using namespace std;
string rick[7] = {"Never gonna give you up",
                  "Never gonna let you down",
                  "Never gonna run around and desert you",
                  "Never gonna make you cry",
                  "Never gonna say goodbye",
                  "Never gonna tell a lie and hurt you",
                  "Never gonna stop"};
int check(string str) {
  for (string r : rick) {
    if (str.compare(r) == 0) return 1;
  }
  return 0;
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N, i, cnt;
  cin >> N;
  cin.ignore();
  cnt = 0;
  i = 0;
  while (i < N) {
    string S;
    getline(cin, S);
    cnt += check(S);
    i++;
  }
  cout << (cnt == N ? "No" : "Yes");
  return 0;
}