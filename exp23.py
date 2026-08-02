#include <stdio.h>

int main() {
    int block = 300, process = 200;

    if (block >= process) {
        printf("Process Allocated\n");
        printf("Remaining Memory = %d", block - process);
    } else {
        printf("Memory Not Allocated");
    }

    return 0;
}
