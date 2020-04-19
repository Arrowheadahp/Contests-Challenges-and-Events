#include <stdio.h>
#include <string.h>
#include <math.h>

int convert(char* s) {
    int mul = strlen(s)-1;
    int sum = 0;
    int i = 0;
    while (mul>=0){
        if (s[i]=='1')  sum+= pow(2,mul);
        i++;
        mul--;
    }
    return sum;
}

int main(void) {
	// your code goes here
	char *A, *B;
	gets(A);
	gets(B);
	
	int a = convert(A);
	int b = convert(B);
	
	int c = 0, t;
	
	while(b){
	    t = a&b;
	    a = a^b;
	    b = t<<1;
	    c++;
	}
	printf("%d",c);
	
	return 0;
}

