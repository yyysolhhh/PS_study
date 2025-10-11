import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int N, M;
    static int[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()); // 한 줄을 읽어서 " " \t \n \r \f 기준으로 나눠줌
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        nums = new int[N + 1]; // 하나 크게 만들어주기 -> 투 포인터 편하게 쓸 수 있음

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int low = 0, high = 0, sum = nums[0], minLength = Integer.MAX_VALUE;
        while (true) {
            // sum >= M -> 답, low++
            if (sum >= M) {
                minLength = Math.min(high - low + 1, minLength);
                sum -= nums[low++];
            }
            // sum > M -> low++
            else {
                sum += nums[++high];
            }
            if (high == N) {
                break;
            }
        }
        if (minLength == Integer.MAX_VALUE) {
            System.out.println(0);
        } else {
            System.out.println(minLength);
        }
    }
}
