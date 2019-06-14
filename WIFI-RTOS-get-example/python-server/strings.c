#include <stdio.h>
// #include <conio.h>
#include <string.h>

int main(){
	// char word[100];
	// char sentence[100];
	int valor = 0;
	// char *str = "0123456789";    

	// sentence = "lalala informacao: importante"
	// word = "informacao"
	char sentence[] = "uuuu lalala informacao: 1";
	char word[] = "informacao: ";
	char info[100];
	int sz_sentence = sizeof(sentence);
	int sz_word = sizeof(word);
	char *p = strstr(sentence, word);
	if(p != NULL){
		printf("%s\n", p);
		// sprintf(info, "%.*s\n", 100, p + sz_word - 1);
		sprintf(info, "%.*s\n", 1, p + sz_word - 1);
		valor = atoi(info);
	}
	printf("%d\n", valor);
	return 0;
}

void findainb(char string, char substring){
	char sentence[] = "lalala informacao: importante";
	char word[] = "informacao";
	char *p = strstr(sentence,word);
}