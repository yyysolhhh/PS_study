import java.util.*;

class studentInfo implements Comparable<studentInfo>{
	int num;
	int cnt;
	int timeStamp;
	boolean isIn;

	public studentInfo(int num, int cnt, int timeStamp, boolean isIn) {
		this.num = num;
		this.cnt = cnt;
		this.timeStamp = timeStamp;
		this.isIn = isIn;
	}

	@Override
	public int compareTo(studentInfo o) {
		int comp = Integer.compare(cnt, o.cnt);
		if (comp == 0) {
			return Integer.compare(timeStamp, o.timeStamp);
		} else {
			return comp;
		}
	}
}
public class Main {
	static int N, total;
	static studentInfo[] student;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		total = sc.nextInt();
		student = new studentInfo[101];

		List<studentInfo> frame = new ArrayList<>();
		for (int i = 0; i < total; i++) {
			int num = sc.nextInt();
			if (student[num] == null) {
				student[num] = new studentInfo(num, 0, 0, false);
			}
			if (student[num].isIn) {
				student[num].cnt++;
			} else {
				if (frame.size() == N) {
					Collections.sort(frame);
					studentInfo s = frame.remove(0);
					s.isIn = false;
					s.cnt = 0;
				}
				student[num].cnt = 1;
				student[num].isIn = true;
				student[num].timeStamp = i;
				frame.add(student[num]);
			}
		}
		frame.sort(new Comparator<studentInfo>() {
			@Override
			public int compare(studentInfo o1, studentInfo o2) {
				return (Integer.compare(o1.num, o2.num));
			}
		});
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < frame.size(); i++) {
			sb.append(frame.get(i).num).append(' ');
		}
		String str = sb.toString();
		System.out.println(str);
	}
}