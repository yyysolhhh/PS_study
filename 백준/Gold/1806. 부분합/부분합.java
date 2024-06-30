import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String str = bf.readLine();
        StringTokenizer st = new StringTokenizer(str);
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        String str2 = bf.readLine();
        StringTokenizer st2 = new StringTokenizer(str2);
        int[] series = new int[N+1];
        for (int i = 0; i < N; i++) {
            series[i] = Integer.parseInt(st2.nextToken());
        }

        int l = 0;
        int h = 0;
        int sum = series[0];
        int length = N + 1;
        while (l < N && h < N) {
            int temp = N + 1;
            // sum >= S -> l++, temp
            if (sum >= S) {
                temp = h - l + 1;
                sum -= series[l++];
            } else { // sum < S -> h++
                sum += series[++h];
            }
            // temp < length -> length = temp
            length = Math.min(temp, length);
        }

        if (length == N + 1){
            System.out.println(0);
        } else {
            System.out.println(length);
        }
    }
}
