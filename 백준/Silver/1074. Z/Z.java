import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int N, r, c;
    static int order;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        int size = (int) Math.pow(2, N);
        order = 0;

        search(r, c, size);
        System.out.println(order);
    }

    static void search(int r, int c, int size) {
        if (size == 1)
            return;
        if (r < size / 2 && c < size / 2) {
            search(r, c, size / 2);
        }
        else if (r < size / 2 && c >= size / 2) {
            order += size * size / 4;
            search(r, c - size / 2, size / 2);
        }
        else if (r >= size / 2 && c < size / 2) {
            order += 2 * (size * size / 4);
            search(r - size / 2, c, size / 2);
        }
        else {
            order += 3 * (size * size / 4);
            search(r - size / 2, c - size / 2, size / 2);
        }
    }
}