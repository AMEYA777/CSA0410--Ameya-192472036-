#include <stdio.h>
#include <stdlib.h>

int main() {
    int req[] = {98, 183, 37, 122, 14, 124, 65, 67};
    int head = 53, total = 0;

    printf("Head Movement: %d", head);

    for (int i = 0; i < 8; i++) {
        total += abs(head - req[i]);
        head = req[i];
        printf(" -> %d", head);
    }

    printf("\nTotal Head Movement = %d\n", total);

    return 0;
}
