#include <stdio.h>

int main() {
    FILE *fp;
    char ch;

    fp = fopen("test.txt", "w");
    fprintf(fp, "Hello File Management");
    fclose(fp);

    fp = fopen("test.txt", "r");
    while ((ch = fgetc(fp)) != EOF)
        putchar(ch);
    fclose(fp);

    printf("\nFile created, written and read successfully.");
    return 0;
}
