#include <bits/stdc++.h>
using namespace std;

int main(void) {
  int N;
  cin >> N;
  queue<int> Q;
  while (N--) {
    string cmd;
    cin >> cmd;
    if (cmd == "push") {
      int num;
      cin >> num;
      Q.push(num);
    } else if (cmd == "pop") {
      if (Q.empty()) {
        cout << -1 << '\n';
      } else {
        cout << Q.front() << '\n';
        Q.pop();
      }
    } else if (cmd == "size") {
      cout << Q.size() << '\n';
    } else if (cmd == "empty") {
      cout << Q.empty() << '\n';
    } else if (cmd == "front") {
      if (Q.empty()) {
        cout << -1 << '\n';
      } else {
        cout << Q.front() << '\n';
      }
    } else if (cmd == "back") {
      if (Q.empty()) {
        cout << -1 << '\n';
      } else {
        cout << Q.back() << '\n';
      }
    }
  }
}