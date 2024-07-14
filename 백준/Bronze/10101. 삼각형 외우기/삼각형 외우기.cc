#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int ang1, ang2, ang3;
  cin >> ang1 >> ang2 >> ang3;
  if (ang1 + ang2 + ang3 == 180) {
    if (ang1 == 60 && ang2 == 60 && ang3 == 60) {
      cout << "Equilateral";
    } else if (ang1 != ang2 && ang1 != ang3 && ang2 != ang3) {
      cout << "Scalene";
    } else {
      cout << "Isosceles";
    }
  } else {
    cout << "Error";
  }
  return 0;
}