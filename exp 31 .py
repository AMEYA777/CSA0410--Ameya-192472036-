#include <stdio.h>

int main() {
    int pages[] = {1, 2, 3, 1, 4, 5};
    int frame[3], i, j, pos = 0, fault = 0, found;

    for (i = 0; i < 3; i++)
        frame[i] = -1;

    for (i = 0; i < 6; i++) {
        found = 0;

        for (j = 0; j < 3; j++)
            if (frame[j] == pages[i])
                found = 1;

        if (!found) {
            frame[pos] = pages[i];
            pos = (pos + 1) % 3;
            fault++;
        }
    }

    printf("Page Faults = %d", fault);
    return 0;
}
