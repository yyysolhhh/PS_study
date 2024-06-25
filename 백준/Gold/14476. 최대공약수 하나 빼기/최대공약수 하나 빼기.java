import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[] nums;
    static int[] gcdLtoR;
    static int[] gcdRtoL;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        nums = new int[N];
        gcdLtoR = new int[N];
        gcdRtoL = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        gcdLtoR[0] = nums[0];
        gcdRtoL[N - 1] = nums[N - 1];
        for (int i = 1; i < N; i++) {
            gcdLtoR[i] = gcd(gcdLtoR[i - 1], nums[i]);
        }
        for (int i = N - 2; i >= 0; i--) {
            gcdRtoL[i] = gcd(gcdRtoL[i + 1], nums[i]);
        }

        int max = 0;
        int maxIndex = 0;
        for (int i = 0; i < N; i++) {
            int gcd = 0;
            if (i == 0) {
                gcd = gcdRtoL[1];
            } else if (i == N - 1) {
                gcd = gcdLtoR[N - 2];
            } else {
                gcd = gcd(gcdLtoR[i - 1], gcdRtoL[i + 1]);
            }

            // k가 gcd로 나눠지면 안됨
            if (nums[i] % gcd != 0 && gcd > max) {
                max = gcd;
                maxIndex = i;
            }
        }

        if (max == 0) {
            System.out.println(-1);
        } else{
            System.out.println(max + " " + nums[maxIndex]);
        }

    }

    // gcd( a, b ) == gcd( b, a % b ), stop when a % b == 0
    static int gcd(int a, int b) {
        while (b != 0) {
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
}
