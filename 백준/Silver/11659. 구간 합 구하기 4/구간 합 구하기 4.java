import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException {
        StringTokenizer st;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int Number [] = new int [N+1];
        int D [] = new int [N+1];

        // 입력
        st = new StringTokenizer(br.readLine(), " ");
        for(int i = 1 ; i <= N ; i++) {
            Number[i] = Integer.parseInt(st.nextToken());
        }

        // 점화식을 이용한 계산
        for(int i = 1 ; i <= N ; i++) {
            D[i] = Number[i] + D[i-1];
        }

        // 정답찾기
        int from, to, Answer;
        for(int i = 1 ; i <= M ; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            from = Integer.parseInt(st.nextToken());
            to = Integer.parseInt(st.nextToken());
            Answer = D[to] - D[from - 1];
            bw.write(Answer + "\n");
        }
        bw.flush();
        bw.close();

    }
}