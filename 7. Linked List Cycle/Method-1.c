/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode *follow = head;
    struct ListNode *move = head;
    
    while(move && move -> next)
    {
        follow = follow -> next;
        move = move -> next -> next;
        if(move == follow)
            return 1;
    }
    return 0;
    
}