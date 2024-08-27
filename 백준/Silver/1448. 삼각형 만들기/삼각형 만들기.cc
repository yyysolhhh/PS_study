#include <cstdio>
#include <algorithm>
using namespace std;
int straw[1000000];
int main(void){
	int N, answer=-1;
	scanf("%d", &N);
	for(int i=0; i<N; i++){
		scanf("%d",&straw[i]);
	}
	sort(straw, straw+N);
	N--;
	while(N>=2){
		if(straw[N]<straw[N-1]+straw[N-2]){
			answer = straw[N]+straw[N-1]+straw[N-2];
			break;
		}
		N--;
	}
	printf("%d",answer);
}