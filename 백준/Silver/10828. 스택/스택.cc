#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    stack<int> st;
    while (N--) {
        string s;
        cin >> s;

        if (s == "push") {
            int num;
            cin >> num;
            st.push(num);
        } else if (s == "pop") {
            if (!st.empty()) {
                cout << st.top() << '\n';
                st.pop();
            } else
                cout << -1 << '\n';
        } else if (s == "size") {
            cout << st.size() << '\n';
        } else if (s == "empty") {
            cout << st.empty() << '\n';
        } else if (s == "top") {
            if (!st.empty())
                cout << st.top() << '\n';
            else
                cout << -1 << '\n';
        }

    }
}