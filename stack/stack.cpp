/*************************************************************************
	> File Name: seqStack.c
	> Author: alpha
	> Mail: icdmck@163.com
	> Created Time: Wed 07 Dec 2016 11:26:54 PM HKT
 ************************************************************************/

#include "stack.h"

void InitStack(SqStack* s)
{
	/* 时间复杂度O(1) */
	s->top = -1; /* 初始化一个空栈 */
}

/* 插入元素e为新的栈顶元素 */
Status Push(SqStack* s, SElemType e)
{
	/* 本次入栈操作不涉及循环，所以本次操作的时间复杂度为O(1) */
	if (s->top == MAXSIZE - 1) { /* 栈满 */
		return ERROR;
	}
	s->top++;  /* 栈顶指针增加一 */
	s->data[s->top] = e; /* 将新插入元素赋值给栈顶空间 */
	return OK;
}

Status Pop(SqStack* s, SElemType* e)
{
	/* 本次出栈操作不涉及循环语句的使用，所以时间复杂度是O(1) */
	if (s->top == -1) {
		return ERROR;
	}
	*e = s->data[s->top]; /* 将位于栈顶的元素赋值给e */
	s->top--;			/* 栈顶指针减一 */
	return OK;
}

Status IsEmpty(SqStack* s)
{
	if (s->top == -1) {
		return true;
	}
	return false;
}
