import java.io.*;

public class Main {
    static char[] str1;
    static char[] str2;
    static int[][] dpLength;
    static int[][] direction;

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
        direction = new int[len1 + 1][len2 + 1];

        int fromLeft = 1;
        int fromUp = 2;
        int equal = 3;

        for (int i = 1; i <= str1.length; i++) {
            for (int j = 1; j <= str2.length; j++) {
                if (dpLength[i - 1][j] > dpLength[i][j - 1]) {
                    dpLength[i][j] = dpLength[i - 1][j];
                    direction[i][j] = fromUp;
                } else {
                    dpLength[i][j] = dpLength[i][j - 1];
                    direction[i][j] = fromLeft;
                }
                if (str1[i - 1] == str2[j - 1]) {
                    if (dpLength[i][j] < dpLength[i - 1][j - 1] + 1)  {
                        dpLength[i][j] = dpLength[i - 1][j - 1] + 1;
                        direction[i][j] = equal;
                    }
                }
            }
        }

        StringBuffer LCS = new StringBuffer();
        int i = len1, j = len2;
        while (i >= 1 && j >= 1) {
            if (direction[i][j] == fromUp) {
                i--;
            }
            else if (direction[i][j] == fromLeft) {
                j--;
            }
            else if (direction[i][j] == equal) {
                LCS.append(str1[i - 1]);
                i--;
                j--;
            }
        }

        bw.write(dpLength[len1][len2] + "\n");
        bw.write(LCS.reverse() + "\n");
        bw.flush();
        bw.close();

    }
}