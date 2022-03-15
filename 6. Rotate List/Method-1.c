/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* rotateRight(struct ListNode* head, int k){
    int cnt = 0,i;
    if (head == NULL)
        return head;
    struct ListNode *p, *temp = NULL,*x;
    p = head;
    while(p != NULL)
    {
        cnt += 1;
        p = p -> next;
    }
    if(cnt == 1)
        return head;
    k = k % cnt;
    for(i = 0; i < k; i++)
    {
        p = head;
        while(p -> next -> next != NULL) p = p -> next;
        temp = p -> next;
        p -> next = NULL;
        temp -> next = head;
        head = temp;
    }
    return head;
}