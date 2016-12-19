#ifndef _STACK_H
#define _STACK_H
#include<stdio.h>

#define MAXSIZE 10
#define OK 1
#define ERROR -1

typedef int Status;
typedef int SElemType;   /* SElemType 类型根据实际情况而定， 这里假设为int*/

typedef struct{
	SElemType data[MAXSIZE];
	int top;  /* 用于栈顶指针 */
}SqStack;

/* The declarations of Each function*/
void InitStack(SqStack* s);
Status Push(SqStack* s, SElemType e);
Status Pop(SqStack* s, SElemType* e);
Status IsEmpty(SqStack* s);

#endif

