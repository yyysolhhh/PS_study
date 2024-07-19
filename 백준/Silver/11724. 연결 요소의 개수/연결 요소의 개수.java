import java.util.Scanner;

public class Main {
		static int N;
		static int M;
		static int[][] map;
		static boolean[] visited;
		
	public static void DFS(int i) {
		visited[i] = true;

		for (int j = 1; j < N+1; j++) {
			if (map[i][j] == 1 && visited[j] == false) {
				DFS(j);		
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		int res = 0;
		
		map = new int[N+1][N+1];
		visited = new boolean[N+1];
		
		for (int i = 0; i < M; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			map[u][v] = map[v][u] = 1;
		}
		
		for (int i = 1; i < N+1; i++) {
			if (visited[i] == false) {
				DFS(i);
				res++;
				
			}
		}
		System.out.println(res);
		sc.close();
	
	}

}