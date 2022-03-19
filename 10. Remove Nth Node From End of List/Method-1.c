/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode *move = head;
    int cnt = 0,i;
    if(head -> next == NULL && n == 1) return NULL;
    while(move != NULL)
    {
        cnt++;
        move = move -> next;
    }
    if(cnt == n) return head -> next;
    move = head;
    for(i = 1; i <= cnt - n - 1; i++) move = move -> next;
    move -> next = move -> next -> next;
    return head;
}