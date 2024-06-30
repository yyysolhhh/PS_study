import java.io.*;

public class Main {
    static char[] str1;
    static char[] str2;
    static int[][] dpLength;
    static int ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s1 = br.readLine();
        String s2 = br.readLine();
        str1 = s1.toCharArray();
        str2 = s2.toCharArray();
        int len1 = str1.length;
        int len2 = str2.length;

        dpLength = new int[len1 + 1][len2 + 1];

        for (int i = 1; i <= str1.length; i++) {
            for (int j = 1; j <= str2.length; j++) {
                if (str1[i - 1] == str2[j - 1]) {
                    dpLength[i][j] = Math.max(dpLength[i][j], dpLength[i - 1][j - 1] + 1);
                    ans = Math.max(ans, dpLength[i][j]);
                }
            }
        }

        bw.write(ans + "\n");
        bw.flush();
        bw.close();
    }
}