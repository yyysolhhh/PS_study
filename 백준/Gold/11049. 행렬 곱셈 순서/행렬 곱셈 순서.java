import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException {
        StringTokenizer st;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int MatrixR [] = new int [N+1];
        int MatrixC [] = new int [N+1];
        int D [][] = new int [N+1+1][N+1+1];
        final int Inf = Integer.MAX_VALUE;

        for(int i = 1 ; i <= N ; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            MatrixR[i] = Integer.parseInt(st.nextToken());
            MatrixC[i] = Integer.parseInt(st.nextToken());
        }

        for(int i = N-1 ; i >= 1 ; i--) { // from
            for(int j = i + 1 ; j <= N ; j++) { // to
                D[i][j] = Inf;
                for(int k = i ; k <= j ; k++) { // 자르는 위치
                    D[i][j] = Math.min(D[i][j], D[i][k]+D[k+1][j]+MatrixR[i]*MatrixC[k]*MatrixC[j]);
                }
            }
        }

        bw.write(D[1][N] + "\n");
        bw.flush();
        bw.close();

    }
}