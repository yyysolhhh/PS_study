#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin >> t;
	
	while (t--) {
		string s;
		cin >> s;
		list<char> L;
		auto cur = L.begin();
		
		for (auto c : s) {
			if (c == '<') {
				if (cur != L.begin())
					cur--;
			} else if (c == '>') {
				if (cur != L.end())
					cur++;
			} else if (c == '-') {
				if (cur != L.begin()) {
					cur--;
					cur = L.erase(cur);
				}
			} else {
				L.insert(cur, c);
			}
		}
		for (auto c : L)
			cout << c;
        cout << '\n';
	}
}