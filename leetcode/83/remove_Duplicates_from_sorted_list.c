/**
 * Given a sorted linked list, delete all duplicates such that each element
 * appear only once.
 * 
 * Example 1 :
 * 
 * Input : 1->1->2
 * Output : 1->2
 * 
 * Example 2 :
 * 
 * Input : 1->1->2->3->3
 * Output : 1->2->3
 * 
 */

#include <stdio.h>
#include <stdlib.h>

/**
 * Definition for singly-linked list.
 */

struct ListNode
{
    int val;
    struct ListNode *next;
};

typedef struct ListNode Node;
struct ListNode *deleteDuplicates(struct ListNode *head)
{
    Node *node1 = head;
    Node *node2 = head->next;
    while (node2 != NULL)
    {
        Node *nxt = node2->next;
        if (node1->val == node2->val)
        {
            node1->next = nxt;
            node2 = nxt;
        }
        else
        {
            node1 = node2;
            node2 = nxt;
        }
    }
    return head;
}

int main()
{
    Node *head = (Node *)malloc(sizeof(Node));
    head->val = 1;
    head->next = (Node *)malloc(sizeof(Node));
    head->next->val = 1;
    head->next->next = (Node *)malloc(sizeof(Node));
    head->next->next->val = 2;
    Node *h = deleteDuplicates(head);
    Node *cur = h;
    while (1)
    {
        h = h->next;
        printf("%d ", cur->val);
        if (h == NULL)
        {
            printf("%d\n", cur->val);
            break;
        }
    }
    return 0;
}