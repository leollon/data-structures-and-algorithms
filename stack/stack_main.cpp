#include "stack.h"

int main(int argc, char** argv) {
    int elem;
    SqStack stack;
    InitStack(&stack);
    /* 入栈操作 */
    while(scanf("%d", &elem) != EOF) {
        int status = Push(&stack, elem);
        //printf("%d ", elem);
        if (status < 0) {
            printf("push error!\n");
            break;
        }
    }

    putchar('\n');
    while(Pop(&stack, &elem) != -1) {
        printf("%d ", elem);
    }
    printf("\n");
    return 0;
}
