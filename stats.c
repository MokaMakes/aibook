#include <stdio.h>
#include <sys/stat.h>
#include <time.h>
#include <pwd.h>
#include <grp.h>

void print_file_stats(const char *filename) {
    struct stat st;
    if (stat(filename, &st) == -1) {
        perror("stat");
        return;
    }

    // File type and permissions
    printf("File: %s\n", filename);
    printf("Size: %lld bytes\n", (long long)st.st_size);
    printf("Blocks: %lld\tBlock size: %ld bytes\n", (long long)st.st_blocks, (long)st.st_blksize);
    printf("Inode: %llu\n", (unsigned long long)st.st_ino);
    printf("Permissions: %o (octal)\n", st.st_mode & 0777);
    printf("Owner UID: %u\tGroup GID: %u\n", st.st_uid, st.st_gid);

    // Get owner and group names
    struct passwd *pw = getpwuid(st.st_uid);
    struct group *gr = getgrgid(st.st_gid);
    printf("Owner: %s\tGroup: %s\n", pw ? pw->pw_name : "unknown", gr ? gr->gr_name : "unknown");

    // Timestamps
    printf("Last access: %s", ctime(&st.st_atime));
    printf("Last modification: %s", ctime(&st.st_mtime));
    printf("Last status change: %s", ctime(&st.st_ctime));
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1;
    }
    print_file_stats(argv[1]);
    return 0;
}