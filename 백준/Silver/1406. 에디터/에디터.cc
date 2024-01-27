#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	string s;
	cin >> s;
	list<char> L;
	for (auto c : s)
		L.push_back(c);
	list<char>::iterator cur = L.end();

	int M;
	cin >> M;
	while (M--) {
		char cmd;
		cin >> cmd;
		if (cmd == 'P') {
			char c;
			cin >> c;
			L.insert(cur, c);
		} else if (cmd == 'L') {
			if (cur != L.begin())
				cur--;
		} else if (cmd == 'D') {
			if (cur != L.end())
				cur++;
		} else if (cmd == 'B') {
			if (cur != L.begin()){
				cur--;
				cur = L.erase(cur);
			}
		}
	}
	for (auto c : L)
		cout << c;
}