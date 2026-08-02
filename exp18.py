#include <stdio.h>

int main() {
    int empty = 1, full = 0;

    if (empty) {
        printf("Producer produced an item\n");
        empty = 0;
        full = 1;
    }

    if (full) {
        printf("Consumer consumed the item\n");
        full = 0;
        empty = 1;
    }

    return 0;
}
