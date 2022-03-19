/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode *dummy, *start;
    start = (struct ListNode*)malloc(sizeof(struct ListNode));
    start -> next = head;
    dummy = start; 
    while(n--)
        head = head -> next;
    while(head)
    {
        head = head -> next;
        dummy = dummy -> next;
    }   
    dummy -> next = dummy -> next -> next;
    return start -> next;
}