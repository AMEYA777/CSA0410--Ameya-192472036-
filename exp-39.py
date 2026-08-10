#include <stdio.h>
#include <stdlib.h>

int main() {
    int req[] = {14, 37, 65, 67, 98, 122, 124, 183};
    int head = 53, total = 0;

    printf("Head Movement: %d", head);

    for (int i = 2; i < 8; i++) {
        total += abs(head - req[i]);
        head = req[i];
        printf(" -> %d", head);
    }

    total += 199 - head;
    head = 199;
    printf(" -> %d", head);

    total += 199;
    head = 0;
    printf(" -> %d", head);

    for (int i = 0; i < 2; i++) {
        total += abs(head - req[i]);
        head = req[i];
        printf(" -> %d", head);
    }

    printf("\nTotal Head Movement = %d\n", total);

    return 0;
}
