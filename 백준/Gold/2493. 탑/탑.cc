#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  stack<pair<int, int>> St;
  St.push({100000001, 0});
  for (int i = 1; i <= N; i++) {
    int h;
    cin >> h;
    while (h > St.top().first) {
      St.pop();
    }
    cout << St.top().second << ' ';
    St.push({h, i});
  }
}