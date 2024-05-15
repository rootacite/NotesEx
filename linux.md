# Linux 系统调用笔记

## I/O篇

### truncate

```c
#include <unistd.h>
#include <sys/types.h>

int ftruncate(int fd, off_t len);
int truncate(const char *path, off_t len);
```

截断一个文件，ftruncate对一个文件描述符操作，truncate对一个文件路径所指向的文件操作。当然，这个函数需要**可写**权限。
甚至可以把文件"截断"成比原文件还大，多余的部分系统会用0填充。

```c
#include <unistd.h>
#include <stdio.h>

int main()
{
    int ret;

    ret = truncate("./pirate.txt", 45);
    // Cut off "pirate.txt" at offset->45
    if(ret == -1)
    {
        perror("truncate()");
        exit(-1);
    }

    return 0;
}
```

### dup&dup2

```c
#include <unistd.h>

int dup(int oldfd);
int dup2(int oldfd, int newfd);
```

复制一个文件描述符，dup2可以把文件描述符复制到指定的fd号。

```c
#include <unistd.h>
#include <fcntl.h>

int main()
{
    int fd = open("./log.txt", O_RDWR|O_CREAT);

    dup2(fd, 1);    // 将stdout重定向到文件
    printf("Writen String %s\n", "HaHAhaha");

    close(fd);
}
```

### select&poll （I/O多路复用）

#### select()

```c
#include <sys/select.h>
#include <sys/time.h>

int select(int n, fd_set *readfds, fd_set *writefds, fd_set *exceptfds, timeval *timeout);

FD_CLR(int fd, fd_set *set);    //oops, you 'd better don't to use it.
FD_ISSET(int fd, fd_set *set);
FD_SET(int fd, fd_set *set);
FD_ZERO(fd_set *set);

struct timeval {
    long tv_sec;   // second
    long tv_usec;  // micro second
}
```

* n: select接受的fds中的所有文件描述符的最大值再+1
* readfds/writefds/exceptfds: 监测这些fds中的描述符是否 **可读/可写/发生异常**
* timeout: 超时时间

select监测所选的文件描述符中，是否有一个或多个描述符进入了我们所期待的状态。

* 若有，则返回他们的数目
* 若等待的时间超出了我们指定的超时时间，则返回0
* 若发生了错误，则返回-1

在成功返回的情况中，每个集合都会被修改成只包含**相应的进入了我们所期待的状态的描述符**，此时可以用FD_ISSET去检查

* FD_ZERO 清空指定的文件描述符集合
* FD_SET  将一个指定的文件描述符置入到指定的集合中

Eg：

```cpp
#include <iostream>
#include <cstdio>
#include <atomic>

using namespace std;
// No Multithreading

int main() {
    char buf[255];
    int fd = 0; // Stdin

    while(1)
    {
        fd_set rfd;
        timeval t{.tv_sec=1, .tv_usec=0};

        FD_ZERO(&rfd);   // Init fd collection
        FD_SET(fd, &rfd); // Set stdin to rfd

        int cn = select(1, &rfd, nullptr, nullptr, &t);

        if(cn == -1)break;
        if(cn == 0){ continue; } // Time Out

        if(FD_ISSET(fd, &rfd)) // If fd "0" is in result collection
        {
            ssize_t sz = read(fd, buf, 255);
            write(1, buf, sz);
        }
    }
    return 0;
}
```

#### poll()

```cpp
#include <poll.h>

int poll(pollfd *fds, nfds_t nfds, int timeout);

struct pollfd
{
    int fd;
    short events;
    short revents
}
```

poll的使用比select更加简洁和方便

* fds: 一个指向**struct pollfd**结构序列的指针
* nfds: fds指向的序列包含了多少实体
* timeout: 超时时间(ms)

**pollfd**中的**events**字段是一些位的组合，每个位代表了一个事件。比如POLLIN, POLLOUT。类似于select()，如果events中的事件实际成立了，对应的位会在revent中被置1。
需要指出的是，不必每次调用poll时都重新构造pollfd结构。在必要的时候，内核会把revents清空。

```c
#include <unistd.h>
#include <poll.h>

int main() {
    char buf[255];
    int fd = 0; // Stdin

    pollfd fds[] = {
        {.fd = fd, .events = POLLIN, .revents = 0 }     // Item 0
        };

    while(1)
    {
        int cn = poll(fds, 1, 1000);                    // Wait 1000ms for stdin readable

        if(cn == -1) break;
        if(cn == 0){ continue; } // Time Out

        if(fds[0].revents & POLLIN)
        {
            ssize_t sz = read(fd, buf, 255);
            write(1, buf, sz);
        }
    }
    return 0;
}
```

### mmap&munmap&mprotect&msync (mman系列)

#### mmap

```c
#include <sys/mman.h>

void *mmap(
    void *addr, // Most users pass "nullptr" to this
    size_t len, // Mount "len" bytes of the file pointed by "fd"
    int port,   // Can be one of PROT_READ, PROT_WRITE, PROT_EXEC
    int flags,  // MAP_FIXED, MAP_SHARED, MAP_PRIVATE
    int fd,     // file descriptor
    off_t offsets); // offset in file
```

若MAP_PRIVATE被指定，对映射的内存区域的修改不会作用在原文件上。且系统会使用**写时复制**机制来管理这些内存页。若仅仅对映射区域进行读操作，则系统会不同进程的映射区域指向同一块物理内存。只有在一个进程试图进行写操作时，系统才会将对应的内存页复制到进程的私有内存空间。

需要指出的是，**addr**和**offset**参数都必须与系统的内存页大小对齐。比较推荐用POSIX标准定义的方式去获取页大小:

```c
long page_size = sysconf(_SC_PAGESIZE);
```

#### munmap

```c
#include <sys/mman.h>

int munmap(void *addr, size_t len);
```

解除一个被mmap创建的映射。传入相同的addr和len即可，这里的addr是mmap返回的。

#### mprotect

```c
#include <sys/mman.h>

int mprotect(
    const void *addr,
    size_t      len,
    int         prot); // Can be one of PROT_READ, PROT_WRITE, PROT_EXEC
```

该调用可以改变一个指定的内存页的保护属性。在某些系统上，mprotect只能修改由mmap映射的内存区域的属性，但在linux中，他**可以修改任意一个内存页的保护属性**。
很显然，**addr**参数必须与系统的页边界对齐。

#### msync

```c
#include <sys/mman.h>

int msync(
    void   *addr,
    size_t len,
    int    flags);
```

与 **fsync()** 有十分甚至九分的相似，用法也很简单:

```c
if (msync(addr, len, MS_ASYNC) == -1)
{
    perror("msync");
}
```

## 内存管理篇

### 