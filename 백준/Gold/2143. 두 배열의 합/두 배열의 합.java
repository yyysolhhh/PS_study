import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        int N = Integer.parseInt(br.readLine());
        int[] inputA = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            inputA[i] = Integer.parseInt(st.nextToken());
        }

        int M = Integer.parseInt(br.readLine());
        int[] inputB = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            inputB[i] = Integer.parseInt(st.nextToken());
        }

        List<Long> subA = new ArrayList<>();
        List<Long> subB = new ArrayList<>();

        // subA 구하기
        for (int i = 0; i < N; i++) {
            long sum = inputA[i];
            subA.add(sum);
            for (int j = i+1; j < N; j++) {
                sum += inputA[j];
                subA.add(sum);
            }
        }

        // subB 구하기
        for (int i = 0; i < M; i++) {
            long sum = inputB[i];
            subB.add(sum);
            for (int j = i+1; j < M; j++) {
                sum += inputB[j];
                subB.add(sum);
            }
        }

        // subA, subB 정렬하기
        Collections.sort(subA);
        Collections.sort(subB, Comparator.reverseOrder());

        long result = 0;
        int ptA = 0;
        int ptB = 0;
        while (ptA < subA.size() && ptB < subB.size()) {
            long currentA = subA.get(ptA);
            long target = T - currentA;
            //  currentB == target -> subA, subB 같은 수 개수 체크 -> 답 구하기, ptA+, ptB+
            if (subB.get(ptB) == target) {
                long countA = 0;
                long countB = 0;
                while (ptA < subA.size() && subA.get(ptA) == currentA) {
                    countA++;
                    ptA++;
                }
                while (ptB < subB.size() && subB.get(ptB) == target) {
                    countB++;
                    ptB++;
                }
                result += countA * countB;
            }
            //  currentB > target -> ptB++
            else if (subB.get(ptB) > target) {
                ptB++;
            }
            //  currentB < target -> ptA++
            else {
                ptA++;
            }
        }
        System.out.println(result);
    }
}
