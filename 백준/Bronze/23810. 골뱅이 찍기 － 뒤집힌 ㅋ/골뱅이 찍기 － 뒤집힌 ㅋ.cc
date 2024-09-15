#include <bits/stdc++.h>
using namespace std;
void print_hor(int N) {
  for (int i = 0; i < N; i++) {
    for (int i = 0; i < N; i++) {
      cout << "@@@@@";
    }
    cout << "\n";
  }
}
void print_ver(int N) {
  for (int i = 0; i < N; i++) {
    for (int i = 0; i < N; i++) {
      cout << "@";
    }
    cout << '\n';
  }
}
int main(void) {
  int N;
  cin >> N;
  print_hor(N);
  print_ver(N);
  print_hor(N);
  print_ver(N);
  print_ver(N);
  return 0;
}