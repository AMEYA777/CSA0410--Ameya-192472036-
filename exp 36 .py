#include <stdio.h>

int main() {
    int n, block[20];

    printf("Enter number of blocks: ");
    scanf("%d", &n);

    printf("Enter block numbers:\n");

    for (int i = 0; i < n; i++)
        scanf("%d", &block[i]);

    printf("\nLinked Allocation:\n");

    for (int i = 0; i < n; i++) {
        printf("%d", block[i]);

        if (i < n - 1)
            printf(" -> ");
    }

    printf(" -> NULL\n");

    printf("First Block = %d\n", block[0]);
    printf("Last Block = %d\n", block[n - 1]);

    return 0;
}
