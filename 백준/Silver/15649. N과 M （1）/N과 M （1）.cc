#include <bits/stdc++.h>
using namespace std;
int N, M;
vector<int> perm;
void print() {
  for (int i = 0; i < M; i++) {
    cout << perm[i] << ' ';
  }
  cout << '\n';
}
void permutation() {
  if (perm.size() == M) {
    print();
    return;
  }
  for (int i = 1; i <= N; i++) {
    if (find(perm.begin(), perm.end(), i) != perm.end()) continue;
    perm.push_back(i);
    permutation();
    perm.pop_back();
  }
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> M;
  permutation();
  return 0;
}