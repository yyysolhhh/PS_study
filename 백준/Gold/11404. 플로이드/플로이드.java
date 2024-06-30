import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int n, m;
    static int[][] map;
    static StringBuffer ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        StringTokenizer st;

        map = new int[n + 1][n + 1];
        int a, b, c;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            if (map[a][b] == 0 || map[a][b] > c) {
                map[a][b] = c;
            }
        }

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                for (int k = 0; k <= n; k++) {
                    if (j != k && map[j][i] != 0 && map[i][k] != 0) {
                        if (map[j][k] == 0 || map[j][k] > map[j][i] + map[i][k]) {
                            map[j][k] = map[j][i] + map[i][k];
                        }
                    }
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            ans = new StringBuffer();
            for (int j = 1; j <= n; j++) {
                ans.append(map[i][j]).append(" ");
            }
            bw.write(ans + "\n");

        }
        bw.flush();
        bw.close();
    }
}