/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* middleNode(struct ListNode* head){
    int cnt = 0, i;
    struct ListNode *temp;
    temp = head;
    while(temp != NULL)
    {
        cnt++;
        temp = temp -> next;
    }
    temp = head;
    for(i = 0; i < cnt/2; i++)
        temp = temp -> next;
    return temp;

}