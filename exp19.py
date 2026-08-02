#include <stdio.h>

int main() {
    int mutex = 1;

    if (mutex) {
        mutex = 0;
        printf("Process 1 entered Critical Section\n");

        mutex = 1;
        printf("Process 1 exited Critical Section\n");
    } else {
        printf("Resource Busy\n");
    }

    return 0;
}
