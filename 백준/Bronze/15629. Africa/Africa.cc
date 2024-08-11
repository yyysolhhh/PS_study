#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  int ans = 0;
  bool sa = false, zim = false, zam = false;
  for (int i = 0; i < N; i++) {
    string w;
    cin >> w;
    if (w == "botswana") {
      ans += 0;
    } else if (w == "south-africa") {
      sa = true;
    } else if (w == "namibia") {
      if (sa)
        ans += 40;
      else
        ans += 140;
    } else if (w == "zimbabwe") {
      zim = true;
      if (zam) {
        ans += 0;
      } else {
        ans += 30;
      }
    } else if (w == "zambia") {
      zam = true;
      if (zim) {
        ans += 20;
      } else {
        ans += 50;
      }
    } else {
      ans += 50;
    }
    if (w != "zambia" && w != "zimbabwe") {
      zam = false;
      zim = false;
    }
  }
  cout << ans;
  return 0;
}