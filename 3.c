#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>




int main() {
    char* pargv[4]={"ls","-l","newfile",NULL}; 
    int ipt;
    int fd;
    while(1)
    {
        printf("-------------\n");
        printf("0.退出程序\n");
        printf("1.创建文件\n");
        printf("2.写入文件\n");
        printf("3.读取文件\n");
        printf("4.修改权限\n");
        printf("5.查看权限\n");
        printf("-------------\n");
        printf("请选择：\n");
        scanf("%d",&ipt);
        printf("\n");
        switch (ipt)
        {
            case 0:
                close(fd);
                exit(0);
            case 1:
                fd = open("newfile",O_RDWR|O_CREAT,0750);
                if(fd == -1){
                    printf("File Create Failed\n");
                    printf("\n");
                }
                else{
                    printf("文件标识符：\n");
                    printf("fd = %d\n",fd);
                    printf("\n");
                }
                break;
            case 2:
            {
                printf("输入要写的内容：\n");
                char buffer1[1024];
                memset(buffer1,0,1024);
                scanf("%s",buffer1);
                buffer1[strlen(buffer1)]='\n';
                lseek(fd,0,SEEK_END);
                write(fd,buffer1,strlen(buffer1));
                printf("\n");
                break;
            }
            case 3:
            {       
                int num2;
                char buffer2[1024];
                memset(buffer2,0,1024);
                lseek(fd,0,SEEK_SET);
                read(fd,buffer2,1024);
                printf("文件内容：\n");
                printf("%s",buffer2);
                printf("\n");
                break;
            }
            case 4:{
                int i;
                printf("0. 用户可读写执行\n");
                printf("1. 用户只可读\n");
                printf("2. 用户只可写\n");
                printf("3. 用户只可执行\n");
                printf("4. 用户组可读写执行\n");
                printf("5. 用户组只可读\n");
                printf("6. 用户组只可写\n");
                printf("7. 用户组只可执行\n");
                printf("8. 其他用户可读写执行\n");
                printf("9. 其他用户只可读\n");
                printf("10. 其他用户只可写\n");
                printf("11. 其他用户只可执行\n");
                printf("请选择：\n");
                scanf("%d",&i);
                printf("\n");
                switch(i){
                    case 0:chmod("newfile",S_IRWXU);break;
                    case 1:chmod("newfile",S_IRUSR);break;
                    case 2:chmod("newfile",S_IWUSR);break;
                    case 3:chmod("newfile",S_IXUSR);break;
                    case 4:chmod("newfile",S_IRWXG);break;
                    case 5:chmod("newfile",S_IRGRP);break;
                    case 6:chmod("newfile",S_IWGRP);break;
                    case 7:chmod("newfile",S_IXGRP);break;
                    case 8:chmod("newfile",S_IRWXO);break;
                    case 9:chmod("newfile",S_IROTH);break;
                    case 10:chmod("newfile",S_IWOTH);break;
                    case 11:chmod("newfile",S_IXOTH);break;
                    default:printf("error choice!\n");printf("\n");
                }
                printf("更改成功！\n");
                printf("\n");
                break;
            }
            case 5:
                execv("/bin/ls",pargv);
                break;
            default:
                printf("?\n\n");
        }
    }
    return 0;
}
