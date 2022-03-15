/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeElements(struct ListNode* head, int val){
    struct ListNode *p, *q;
    if (head == NULL) return NULL;
    if (head->next == NULL && head->val == val)    return NULL;
    else if (head->next == NULL)   return head;
    p = head;
    q = head;
    while(p != NULL)
    {
        if(p -> val == val)
        {
            q -> next = p -> next;
            p = q -> next;
        }
        else
        {
            q = p;
            p = p -> next;
        }
    }
    if(head->val == val && head->next)
        return head->next;
    else if (head->val == val && !head->next)
        return NULL;
    return head;
}