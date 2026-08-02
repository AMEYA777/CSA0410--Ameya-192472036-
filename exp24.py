#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd;

    fd = open("sample.txt", O_CREAT | O_WRONLY, 0644);

    if (fd != -1) {
        write(fd, "Hello", 5);
        close(fd);
        printf("File Created and Data Written");
    } else {
        printf("Error Opening File");
    }

    return 0;
}
