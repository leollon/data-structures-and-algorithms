#ifndef _LINKLIST_H

#include <stdio.h>
#include <stdlib.h>

typedef struct LinkList {
    int ele;
    struct LinkList *pNext;
}Node, *pNode;

#endif

void printLinkList(pNode);
void initNode(pNode);
void reverseLinkList(pNode);
void createLinkList(pNode);

