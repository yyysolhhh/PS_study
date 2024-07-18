#include<bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int solution(vector<vector<int> > maps)
{
    int n = maps.size();
    int m = maps[0].size();
    int dist[n][m];
    for (int i = 0; i < n; i++) {
        fill(dist[i], dist[i] + m, 0);
    }
    queue<pair<int, int>> Q;
    Q.push({0, 0});
    dist[0][0] = 1;
    while (!Q.empty()) {
       	auto cur = Q.front();
        Q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = cur.X + dx[i];
            int ny = cur.Y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (dist[nx][ny] > 0 || maps[nx][ny] == 0) continue;
            dist[nx][ny] = dist[cur.X][cur.Y] + 1;
            Q.push({nx, ny});
        }
    }
    if (dist[n - 1][m - 1] > 0) return dist[n - 1][m - 1];
    else return -1;
}