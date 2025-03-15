#include <bits/stdc++.h>
using namespace std;
int N, M;
map<string, bool> d;
string s;
vector<string> b;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    cin >> s;
    d.insert(make_pair(s, true));
  }
  for (int i = 0; i < M; i++) {
    cin >> s;
    if (d[s]) {
      b.push_back(s);
    }
  }
  sort(b.begin(), b.end());
  cout << b.size() << '\n';
  for (string s : b) {
    cout << s << '\n';
  }
}