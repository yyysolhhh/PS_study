import java.util.Scanner;

public class Main {
	static int num, pair, res;
	static int[][] map;
	static boolean[] visited;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		num = sc.nextInt();
		pair = sc.nextInt();
		res = 0;
		
		map = new int[num+1][num+1];
		visited = new boolean[num+1];
		
		for (int i = 0; i < pair; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			map[u][v] = map[v][u] = 1;			
		}
		
		dfs(1);
		System.out.println(res);
		
		
	}
	
	public static void dfs(int i) {
		visited[i] = true;
		for (int j = 0; j < num+1; j++) {
			if (map[i][j] == 1 && !visited[j]) {
				dfs(j);
				res++;
			}
			
		}
	}

}
