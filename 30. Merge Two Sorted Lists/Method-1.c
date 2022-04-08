if(!list1) return list2;
if(!list2) return list1;
struct ListNode *move1 = list1, *move2 = list2;
struct ListNode *START, *move;
START = (struct ListNode *)malloc(sizeof(struct ListNode));
move = START;
while(move1 != NULL && move2 != NULL)
{
    if(move1 -> val < move2 -> val)
    {
        move -> next = move1;
        move1 = move1 -> next;
    }
    else
    {
        move -> next = move2;
        move2 = move2 -> next;
    }
    move = move -> next;
}
while(move1 != NULL)
{
    move -> next = move1;
    move = move -> next;
    move1 = move1 -> next;
}
while(move2 != NULL)
{
    move -> next = move2;
    move = move -> next;
    move2 = move2 -> next;
}
return START -> next;
