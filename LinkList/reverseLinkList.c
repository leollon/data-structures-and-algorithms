#include "reverseLinkList.h"

void initNode(pNode node)
{
    node->ele = 0;
    node->pNext = NULL;
}

void createLinkList(pNode head)
{
    int element;
    pNode newNode_1, newNode_2;
    newNode_2 = (pNode) malloc(sizeof(Node));
    if (NULL == head || NULL == newNode_2) {
        return ;
    }

    initNode(head);
    initNode(newNode_2);
    newNode_1 = head;  // 带头节点
    while (scanf("%d", &element) != EOF) {
        newNode_2->ele = element;
        newNode_1->pNext = newNode_2;
        newNode_1 = newNode_2;
        newNode_2 = (pNode) malloc(sizeof(Node));
        if (NULL == newNode_2) {
            break;
        }
        initNode(newNode_2);
    }
    return ;
}

void reverseLinkList(pNode head)
{
    /*****************************
    *   头节点没有放置元素的链表
    ******************************/

    pNode node_1, node_2, tmpNode;
    if (NULL == head) {
        printf("Empty LinkList\n");
        return ;
    }
    node_1 = head->pNext;           // 第一个含有元素的节点指针
    /* 只有一个节点，不需要翻转 */
    if (NULL == node_1->pNext) {
        printf("Only a node, no need to reverse!\n");
        return ;
    }
    node_2 = head->pNext->pNext;    // 紧接着第二个含有元素的节点
    node_1->pNext = NULL;           // 第一个节点指向下一个节点的地址为空
    tmpNode = node_2->pNext;        // 保存链表即将断开的地方

    /* 只含有两个有元素的节点的链表 */
    if (NULL == node_2->pNext) {
        node_2->pNext = node_1;
        node_1->pNext = NULL;
        head->pNext = node_2;
        return ;
    }

    while (NULL != node_2->pNext) {
        node_2->pNext = node_1;     // 后一个节点的指针指向前一个结点
        node_1 = node_2;            // 前一个节点移动到后面的一个结点
        node_2 = tmpNode;           // 结点移动到要反转的链表的子链表的第一个节点
        tmpNode = node_2->pNext;    // 保存当前结点指向下一个结点的指针(地址)
    }
    if (NULL == node_2->pNext) {
        node_2->pNext = node_1;
        head->pNext = node_2;
    }
}


void printLinkList(pNode head)
{
    if (NULL == head || NULL == head->pNext) {
        printf("Empty LinkList！\n");
        return ;
    }
    pNode node = head->pNext;
    for (; node!= NULL; node = node->pNext){
        printf("%d ", node->ele);
    }
}

