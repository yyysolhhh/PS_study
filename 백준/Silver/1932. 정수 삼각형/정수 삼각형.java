import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[][] triangle;
    static int[][] dp;
    static int res;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        triangle = new int[1+ n + 1][1 + n + 1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int j = 1;
            while (st.hasMoreTokens()) {
                triangle[i][j] = Integer.parseInt(st.nextToken());
                j++;
            }
        }

        dp = new int[1 + n + 1][1+ n + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                dp[i][j] = triangle[i][j] + Math.max(dp[i - 1][j - 1], dp[i - 1][j]);
            }
        }

        for (int i : dp[n]) {
            res = Math.max(res, i);
        }

        System.out.println(res);
    }
}