#include <stdio.h>

int main(void) {
	// your code goes 
	
	int T,m,n,k,f,r,c,i;
	scanf("%d",&T);
	
	while(T--){
	    
	    scanf("%d %d %d",&m,&n,&k);
	    
	    char G[1000000002][1000000002]={'0'};
	    f=0;
	    while(k--){
	        scanf("%d %d",&r,&c);
	        int at[4][2]={{r-1,c},{r+1,c},{r,c-1},{r,c+1}};
	        int a=4;
	        for(i=0;i<4;i++){
	            if (G[at[i][0]][at[i][1]]=='1')   a-=2;
	            
	        }
	        G[r][c]='1';
	        f+=a;
	    }
	printf("%d",f);
	}
	return 0;
}

