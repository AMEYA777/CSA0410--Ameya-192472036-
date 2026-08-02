#include <stdio.h>
int main() {
    int read = 1, write = 0;

    if (read)
        printf("Reader is reading the data\n");

    if (!write)
        printf("Writer is waiting\n");

    write = 1;
    printf("Writer is writing the data\n");

    return 0;
}
