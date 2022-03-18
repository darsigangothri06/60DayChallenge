/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode *move;
    move = head;
    while(move && move -> next != NULL)
    {
        if(move -> val == move -> next -> val)
        {
            move -> next = move -> next -> next;
            continue;
        }
        move = move -> next;
    }
    return head;
}