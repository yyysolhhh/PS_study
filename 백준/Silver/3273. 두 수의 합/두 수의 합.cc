#include <bits/stdc++.h>
using namespace std;

int cnt[2000000];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n, x, res = 0;
  cin >> n;
  int seq[n];
  for (int i = 0; i < n; i++) {
    cin >> seq[i];
  }
  cin >> x;
  for (int i = 0; i < n; i++) {
    if (x - seq[i] > 0 && cnt[x - seq[i]])
      res++;
    cnt[seq[i]] = 1;
  }
  cout << res;
}