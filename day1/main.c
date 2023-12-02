#include <stdio.h>  
#include <ctype.h>
#include <string.h>

FILE*fp = NULL;
const char *numbers[] = {"zero", "one", "two", "three", "four", "five",
                             "six", "seven", "eight", "nine"};

int convertStringToNumber(char *str, int idx) {
    for (int i = 0; i < 10; i++) {
        if (strncmp(str + idx, numbers[i], strlen(numbers[i])) == 0) {
            return i;
        }
    }
    return 0;
}

char *readline(){
    char *line = NULL;
    size_t len = 0;
    ssize_t read;
    if((read = getline(&line, &len, fp)) != -1){
        return line;
    }
    return NULL;    
}
int solve(){
    char c;
    int d1= 0;
    int d2= 0;
    int tmp = 0;
    int sum = 0;
    char *line = NULL;
    while((line = readline()) != NULL){
        for (int i = 0; i < strlen(line); i++){
            c = line[i];
            if(isdigit(c)){
                if(d1 == 0){
                    d1 = c - '0';
                }
                if(d1 != 0){
                    d2 = c - '0';
                }
            }
            if(d1 == 0 ){
                d1 = convertStringToNumber(line, i);
            }
            else{
                tmp = convertStringToNumber(line, i);
            }
            if(tmp != 0){
                d2 = tmp;
            }
        }
        printf("%d %d\n", d1, d2);
        int d = 0;
        d = d1 * 10 + d2;
        sum += d;
        d1 = 0;
        d2 = 0;
    }
    return sum;
}

int main(int argc, char *argv[])
{
    // read file 
    fp = fopen("./input", "r");
    int output = solve();
    printf("output: %d\n", output);
    return 0;
}
