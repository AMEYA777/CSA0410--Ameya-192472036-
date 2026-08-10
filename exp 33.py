#include <stdio.h>

int main() {
    int pages[] = {7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1};
    int frame[3] = {-1,-1,-1};
    int faults = 0;

    for (int i = 0; i < 20; i++) {
        int found = 0;

        for (int j = 0; j < 3; j++) {
            if (frame[j] == pages[i])
                found = 1;
        }

        if (!found) {
            int pos = -1, farthest = -1;

            for (int j = 0; j < 3; j++) {
                int k;

                for (k = i + 1; k < 20; k++) {
                    if (frame[j] == pages[k])
                        break;
                }

                if (k == 20) {
                    pos = j;
                    break;
                }

                if (k > farthest) {
                    farthest = k;
                    pos = j;
                }
            }

            frame[pos] = pages[i];
            faults++;
        }

        printf("\nPage %d : ", pages[i]);
        for (int j = 0; j < 3; j++)
            printf("%d ", frame[j]);
    }

    printf("\n\nTotal Page Faults = %d\n", faults);

    return 0;
}
