/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteMiddle(struct ListNode* head){
    int cnt = 0, i;
    struct ListNode *temp, *follow = NULL;
    temp = head;
    if(head -> next == NULL) return NULL;
    if(head -> next -> next == NULL)
    {
        head -> next = NULL;
        return head;
    }
    while(temp != NULL)
    {
        cnt++;
        temp = temp -> next;
    }
    temp = head;
    for(i = 0; i < cnt/2; i++)
    {
        follow = temp;
        temp = temp -> next;
    }
    follow -> next = temp -> next;
    temp -> next = NULL;
    free(temp);
    return head;

}