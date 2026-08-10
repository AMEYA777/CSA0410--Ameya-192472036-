#include <stdio.h>

int main() {
    int pages[] = {1, 2, 3, 1, 4, 5};
    int frame[3], time[3] = {0}, i, j, pos, fault = 0;
    int found, counter = 0;

    for (i = 0; i < 3; i++)
        frame[i] = -1;

    for (i = 0; i < 6; i++) {
        found = 0;

        for (j = 0; j < 3; j++)
            if (frame[j] == pages[i]) {
                found = 1;
                time[j] = ++counter;
            }

        if (!found) {
            pos = 0;
            for (j = 1; j < 3; j++)
                if (time[j] < time[pos])
                    pos = j;

            frame[pos] = pages[i];
            time[pos] = ++counter;
            fault++;
        }
    }

    printf("Page Faults = %d", fault);
    return 0;
}
