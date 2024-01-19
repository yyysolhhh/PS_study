import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;


public class Main {
	static int[][] map; // 간선 연결 상태
	static boolean[] visited; // 방문 여부 
	static int N; // 정점 개수
	static int M; // 간선 개수 
	static int V; // 시작 정점 

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String s = br.readLine();
		StringTokenizer st = new StringTokenizer(s);
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		V = Integer.parseInt(st.nextToken());
		
		map = new int[1001][1001];
		visited = new boolean[1001];
		
		for (int i = 0; i < M; i++) {
			String s2 = br.readLine();
			StringTokenizer st2 = new StringTokenizer(s2);
			int x = Integer.parseInt(st2.nextToken());
			int y = Integer.parseInt(st2.nextToken());
						
			map[x][y] = map[y][x] = 1;			
		}
		br.close();
		
		dfs(V);
		visited = new boolean[1001];
		System.out.println();
		bfs(V);

	}
	
	public static void dfs(int i) {
		visited[i] = true;
		System.out.print(i + " ");
		for (int j = 0; j < N+1; j++) {
			if (map[i][j] == 1 && visited[j] == false) {
				dfs(j);
			}
			
		}
	}
	
	public static void bfs(int i) {
		Queue<Integer> q = new LinkedList<>();
		q.offer(i);
		visited[i] = true;
		
		while (!q.isEmpty()) {
			int temp = q.poll();
			System.out.print(temp + " ");
			for (int j = 0; j < N+1; j++) {
				if (map[temp][j] == 1 && visited[j] == false) {
					q.offer(j);
					visited[j] = true;
				}
				
			}
		}
	}

}
