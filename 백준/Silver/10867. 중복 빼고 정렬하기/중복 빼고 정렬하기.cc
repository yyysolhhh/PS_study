#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  int nums[N];
  for (int i = 0; i < N; i++) {
    cin >> nums[i];
  }
  sort(nums, nums + N);
  cout << nums[0] << ' ';
  for (int i = 1; i < N; i++) {
    if (nums[i] != nums[i - 1]) {
      cout << nums[i] << ' ';
    }
  }
  return 0;
}