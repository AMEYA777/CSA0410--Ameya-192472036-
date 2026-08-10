#include <stdio.h>
#include <sys/stat.h>

int main() {

    printf("Linux File Permissions\n\n");

    printf("r = Read\n");
    printf("w = Write\n");
    printf("x = Execute\n\n");

    printf("u = Owner\n");
    printf("g = Group\n");
    printf("o = Others\n\n");

    chmod("test.txt", 0644);

    printf("Permission: rw-r--r--\n");
    printf("Owner  : Read + Write\n");
    printf("Group  : Read\n");
    printf("Others : Read\n");

    return 0;
}
