import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static long [] WeightDiff;
    static int [] Parent;
    static long Answer;

    public static void main(String[] args) throws NumberFormatException, IOException {
        StringTokenizer st;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while(true) {
            st = new StringTokenizer(br.readLine()," ");
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            if(N == 0 && M == 0) {
                break;
            }

            WeightDiff = new long [N + 1];
            Parent = new int [N + 1];
            for (int i = 1 ; i <= N ; i++) {
                Parent[i] = i;
            }
            String q;
            int a, b, diff;
            for(int i = 1 ; i <= M ; i++) {
                st = new StringTokenizer(br.readLine()," ");
                q = st.nextToken();
                a = Integer.parseInt(st.nextToken());
                b = Integer.parseInt(st.nextToken());

                if(q.equals("!")) {
                    diff = Integer.parseInt(st.nextToken());
                    union(a, b, diff);
                } else {
                    if(find(a) == find(b)) {
                        Answer = WeightDiff[b] - WeightDiff[a];
                        bw.write(Answer + "\n");
                    } else {
                        bw.write("UNKNOWN" + "\n");
                    }
                }
            }
        }

        bw.flush();
        bw.close();
    }
    private static void union(int a, int b, int diff) {
        int parentA = find(a);
        int parentB = find(b);

        if(parentA == parentB) {
            return;
        }

        WeightDiff[parentB] = WeightDiff[a] - WeightDiff[b] + diff;
        Parent[parentB] = parentA;
    }

    private static int find(int i) {
        if(Parent[i] == i) {
            return i;
        } else {
            int parentIndex = find(Parent[i]);
            WeightDiff[i] += WeightDiff[Parent[i]];
            return Parent[i] = parentIndex;
        }
    }
}