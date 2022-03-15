/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* oddEvenList(struct ListNode* head){
    if(head == NULL ||head -> next == NULL || head -> next -> next == NULL) return head;
    struct ListNode *take, *follow = NULL, *end, *fix, *p;
    int i = 0, cnt = 0;
    take = head;
    while(take -> next != NULL) 
    {take = take -> next;
     cnt += 1;
    }
    cnt += 1;
    fix = take;
    end = take;
    take = head -> next;
    follow = head;
    while(take != fix)
    {
        if(i % 2 == 0)
        {
            follow -> next = take -> next;
            take -> next = NULL;
            end -> next = take;
            end = end -> next;
            take = follow -> next;
            i++;
        }
        else{
            follow = take;
            take = take -> next;
            i++;
        }
    }
    if(cnt % 2== 0)
    {
        follow -> next = take -> next;
        take -> next = NULL;
        end -> next = take;
        end = end -> next;
        take = follow -> next;
    }
    return head;

}