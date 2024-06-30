#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  string a, b, c;
  cin >> a >> b >> c;
  string res;
  int num;
  if (isdigit(c[0])) {
    num = stoi(c) + 1;
    if (num % 3 == 0 && num % 5 == 0) {
      cout << "FizzBuzz";
    } else if (num % 3 == 0) {
      cout << "Fizz";
    } else if (num % 5 == 0) {
      cout << "Buzz";
    } else {
      cout << num;
    }
  } else if (isdigit(b[0])) {
    num = stoi(b) + 2;
    if (num % 3 == 0 && num % 5 == 0) {
      cout << "FizzBuzz";
    } else if (num % 3 == 0) {
      cout << "Fizz";
    } else if (num % 5 == 0) {
      cout << "Buzz";
    } else {
      cout << num;
    }
  } else if (isdigit(a[0])) {
    num = stoi(a) + 3;
    if (num % 3 == 0 && num % 5 == 0) {
      cout << "FizzBuzz";
    } else if (num % 3 == 0) {
      cout << "Fizz";
    } else if (num % 5 == 0) {
      cout << "Buzz";
    } else {
      cout << num;
    }
  }
}