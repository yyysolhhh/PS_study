#include <bits/stdc++.h>
using namespace std;
vector<tuple<int, int, int>> coords;
int N, M;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N;
  int x, y, z, r;
  for (int i = 0; i < N; i++) {
    cin >> x >> y >> z;
    coords.emplace_back(x, y, z);
  }
  cin >> M;
  for (int i = 0; i < M; i++) {
    cin >> x >> y >> z >> r;
    int ans = 0;
    for (auto& [cx, cy, cz] : coords) {
      if (pow(x - cx, 2) + pow(y - cy, 2) + pow(z - cz, 2) <= pow(r, 2)) {
        ans++;
      }
    }
    cout << ans << "\n";
  }
  return 0;
}