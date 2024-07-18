#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int solution(int n, vector<vector<int>> computers) {
    int ans = 0;
    int vis[n][n];
    for (int i = 0; i < n; i++) {
        fill(vis[i], vis[i] + n, 0);
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (!vis[i][j] && computers[i][j]) {
                queue<pair<int, int>> Q;
                Q.push({i, j});
                vis[i][j] = 1;
                vis[j][i] = 1;
                while (!Q.empty()) {
                    auto cur = Q.front(); Q.pop();
                    for (int idx = 0; idx < n; idx++) {
                        int nx = idx;
                        int ny = cur.Y;
                        if (vis[nx][ny] || !computers[nx][ny]) continue;
                        vis[nx][ny] = 1;
                        vis[ny][nx] = 1;
                        Q.push({ny, nx});
                    }
                }
                ans++;
            }
        }
    }
    return ans;
}