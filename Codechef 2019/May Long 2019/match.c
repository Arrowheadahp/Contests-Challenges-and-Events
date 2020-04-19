#include <stdio.h>

int pred(int a,int b,int t){
	if (a%b==0)		return (t);
	
	if (a>(b*2)){
		if ((t==pred(b,a%b,1-t)) || (t==pred(b+a%b,b,1-t)))
			return (t);
		
		return (1-t);
	}
	return (pred(b,a%b,1-t));
}

int main(void) {
	int n,a,b,win;
	
	scanf("%d",&n);
	while(n--){
		scanf("%d %d",&a,&b);
		if (a>b)	win=pred(a,b,0);
		else		win=pred(b,a,0);
		
		if (win==0)	printf("Ari\n");
		else		printf("Rich\n");
	}
	
	return 0;
}
