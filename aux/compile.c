#include<stdio.h>
#include<ctype.h>
#include<stdlib.h>
#include<string.h>

char* DELIM = "<$>";

char* strip(char* s) { // this also manipulates the original string
	int i, j;
	for (i = 0; isspace(s[i]); i++);
	for (j = strlen(s)-1; isspace(s[j]); j--);
	s[j+1] = '\0';
	return &(s[i]);
}

void read_until_delim(FILE* f, char buf[]) { // makes it hard to change the delim. not modular
	int i = 0;
	char c;
	while ( (c = fgetc(f)) != EOF) {
		if (c == DELIM[0]) {
			char next = fgetc(f), nextt = fgetc(f);
			if (next == DELIM[1] && nextt == DELIM[2]) {
				buf[i] = '\0';
				return;
			} else {
				buf[i++] = c; buf[i++] = next; buf[i++] = nextt;
			}
		} else {
			buf[i++] = c;
		}
	}
}

int main(int argc, char *argv[])
{
	if (argc == 1) {
		printf("provide arg\n");
		exit(1);
	}

	FILE* f = fopen(argv[1],"r");
	char* s = malloc(1000);
	read_until_delim(f,s);
	read_until_delim(f,s);
	s = strip(s);
	printf("%s\n",s);
	
	return 0;
}
