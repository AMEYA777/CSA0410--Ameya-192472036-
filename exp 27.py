#include <stdio.h>
#include <dirent.h>

int main() {
    DIR *d;
    struct dirent *file;

    d = opendir(".");
    if (d == NULL) {
        printf("Directory not found");
        return 1;
    }

    while ((file = readdir(d)) != NULL)
        printf("%s\n", file->d_name);

    closedir(d);
    return 0;
}
