import java.util.*;

public class Main {
	static int L, C;
	static char[] data;
	static List<String> result;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		L = sc.nextInt();
		C = sc.nextInt();

		data = new char[C];
		result = new LinkedList<>();

		for (int i = 0; i < C; i++) {
			data[i] = sc.next().charAt(0);
		}

		Arrays.sort(data);
        
		dfs(0, 0, -1, 0, "");

		for (String s : result) {
			System.out.println(s);
		}

	}

	static void dfs(int vowel, int consonant, int curr, int len, String pwd) {
		if (len == L && vowel >= 1 && consonant >= 2) {
			result.add(pwd);
			return;
		}
		for (int i = curr + 1; i < data.length; i++) {
			char next = data[i];
			if (next == 'a' || next == 'e' || next == 'i' || next == 'o' || next == 'u') {
				dfs(vowel + 1,  consonant, i, len + 1, pwd + next);
			} else {
				dfs(vowel, consonant + 1, i, len + 1, pwd + next);
			}
		}
	}
}