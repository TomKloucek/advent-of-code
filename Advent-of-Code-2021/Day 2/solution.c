#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void first_part() {
    FILE* file = fopen("input.txt", "r");
    char line[256];

    int depth = 0;
    int width = 0;

    char way;

    while (fgets(line, sizeof(line), file)) {
        
        char *token = strtok(line, " ");
        way = token[0];

        for(int i = 0; i < 2;i++)
        {
            if (i == 1) {
                int number = atoi(token);
                if (way == 'u') {
                    depth -= number;
                }
                else if (way == 'd') {
                    depth += number;
                }
                else if (way == 'f') {
                    width += number;
                }
                //printf("%d - %d\n",depth,width);
            }
            token = strtok(NULL, " ");
        }

    }
    fclose(file);
    printf("first - %d\n",(depth*width));
}

void second_part() {
    FILE* file = fopen("input.txt", "r");
    char line[256];

    int aim = 0;
    int depth = 0;
    int width = 0;

    char way;

    while (fgets(line, sizeof(line), file)) {
        
        char *token = strtok(line, " ");
        way = token[0];

        for(int i = 0; i < 2;i++)
        {
            if (i == 1) {
                int number = atoi(token);
                if (way == 'u') {
                    aim -= number;
                }
                else if (way == 'd') {
                    aim += number;
                }
                else if (way == 'f') {
                    width += number;
                    depth += (number*aim);
                }
            }
            token = strtok(NULL, " ");
        }

    }
    fclose(file);
    printf("second - %d\n",(depth*width));
}

int main() {
    first_part();
    second_part();
    return 0;
}