import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        MinHeap mh = new MinHeap();

        for (int i = 0; i < N; i++) {
            int input =  Integer.parseInt(br.readLine());
            if (input == 0) {
                System.out.println(mh.delete());
            } else {
                mh.insert(input);
            }
        }
    }
}


class MinHeap {
    List<Integer> list;

    public MinHeap() {
        list = new ArrayList<>();
        list.add(0);
    }

    public void insert(int val) {
        // 1. leaf 마지막에 삽입
        list.add(val);

        int current = list.size() - 1;
        int parent = current / 2;
        // 2. 부모와 비교 후 조건에 맞지 않으면 Swap

        // 3. 조건이 만족되거나 root 까지 반복
        while (true) {
            if (parent == 0 || list.get(parent) <= list.get(current)) {
                break;
            }

            // swap
            int temp = list.get(parent);
            list.set(parent, list.get(current));
            list.set(current, temp);

            current = parent;
            parent = current / 2;
        }
    }

    public int delete() {
        if (list.size() == 1) {
            return 0;
        }
        int top = list.get(1);
        // 1. Root에 leaf 마지막 데이터 가져옴
        list.set(1, list.get(list.size() - 1));
        list.remove(list.size() - 1);

        // 2. 자식과 비교 후 조건이 맞지 않으면 swap
        // 3. 조건이 만족되거나 Leaf 까지 반복
        int currentPos = 1; // current position
        while (true) {
            int leftPos = currentPos * 2;
            int rightPos = currentPos * 2 + 1;

            // 자식 존재 유무 확인
            if (leftPos >= list.size()) { // current가 leaf
                break;
            }

            // 왼쪽 자식 먼저 확인
            int minValue = list.get(leftPos);
            int minPos = leftPos;

            // 오른쪽 자식 확인
            if (rightPos < list.size() && list.get(rightPos) < minValue) {
                minValue = list.get(rightPos);
                minPos = rightPos;
            }

            // Swap
            if (list.get(currentPos) > minValue) {
                int temp = list.get(currentPos);
                list.set(currentPos, list.get(minPos));
                list.set(minPos, temp);
                currentPos = minPos;
            } else {
                break;
            }
        }
        return top;
    }
}
