#include <stdio.h>

int main() {
    int buffer[5], n = 0, choice, item;

    while (1) {
        printf("\n1. Produce  2. Consume  3. Exit\n");
        scanf("%d", &choice);

        if (choice == 1) {
            if (n == 5)
                printf("Buffer Full\n");
            else {
                printf("Enter item: ");
                scanf("%d", &item);
                buffer[n++] = item;
                printf("Produced\n");
            }
        }
        else if (choice == 2) {
            if (n == 0)
                printf("Buffer Empty\n");
            else {
                printf("Consumed: %d\n", buffer[0]);
                for (int i = 0; i < n - 1; i++)
                    buffer[i] = buffer[i + 1];
                n--;
            }
        }
        else
            break;
    }
    return 0;
}
