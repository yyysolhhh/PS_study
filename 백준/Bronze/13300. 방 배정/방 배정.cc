#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N, K, S, Y, res = 0;
	cin >> N >> K;
	int students[7][2] = {};
	while (N--) {
		cin >> S >> Y;
		students[Y][S]++;
	}
	for (auto y: students){
		for (int i = 0; i < 2; i++){
			if (y[i] % K)
				res += y[i] / K + 1;
			else
				res += y[i] / K;
		}
	}
	cout << res;
}