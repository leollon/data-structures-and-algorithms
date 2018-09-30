/*
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order and each of their nodes
 * contain a single digit. Add the two numbers and return it as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 * 
 * Example:
 * 
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
 * Definition for singly-linked list.
 * 
 */
#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

typedef struct ListNode Node;

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    Node *head = (Node *)malloc(sizeof(Node));
    Node *tmp = head;
    tmp->next = NULL;
    Node *p = l1;
    Node *q = l2;
    int carry = 0,
        x = 0,
        y = 0,
        sum = 0;
    while (p || q)
    {
        x = (p != NULL) ? p->val : 0; // 存在后继节点则取后继节点的值，否则为0
        y = (q != NULL) ? q->val : 0; // 同上
        sum = x + y + carry;
        carry = sum / 10;
        Node *new_node = (Node *)malloc(sizeof(Node));
        new_node->next = NULL;
        new_node->val = sum % 10; // 节点的值取求和后取模
        tmp->next = new_node;     // 头节点指向下一个节点
        tmp = new_node;           // 上一个节点到新生成的节点
        p = p ? p->next : NULL;   // 当前节点不为空，移动当前节点到下一个节点
        q = q ? q->next : NULL;   // 同上
    }
    if (carry == 1)
    {
        // 正好遍历到最后一次之前，求和的结果大于10,得新生成一个节点保存进位的值
        Node *new_node = (Node *)malloc(sizeof(Node));
        new_node->next = NULL;
        new_node->val = carry;
        tmp->next = new_node;
    }
    return head->next; // 返回头节点的下一个节点
}

int main()
{
    Node *l1 = (Node *)malloc(sizeof(Node));
    l1->next = NULL;
    l1->val = 1;
    Node *l11 = (Node *)malloc(sizeof(Node));
    l11->next = NULL;
    l1->val = 8;
    l1->next = l11;
    Node *l2 = (Node *)malloc(sizeof(Node));
    l2->next = NULL;
    l2->val = 0;
    Node *list = addTwoNumbers(l1, l2);
    while (list)
    {
        printf("%d\n", list->val);
        list = list->next;
    }
    return 0;
}