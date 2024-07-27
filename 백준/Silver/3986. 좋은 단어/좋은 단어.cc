#include <bits/stdc++.h>
using namespace std;
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    int ans = 0; 
    while (N--) {
        string word;
        cin >> word;
        stack<char> st;
        for (char w: word) {
            if (!st.empty() && w == st.top()) st.pop();
            else st.push(w);
        }
        if (st.empty()) ans++;
    }
    cout << ans;
    return 0;
}