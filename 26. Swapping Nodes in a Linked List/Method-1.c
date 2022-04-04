struct ListNode* swapNodes(struct ListNode* head, int k){
    struct ListNode *temp= head, *temp1 = head, *temp2 = head;
    int count = 0;
    
    // Counting the length of the linked list
    while(temp)
    {
        count++;
        temp=temp->next;
    }
    if(count == 1 && k == 1)
        return head;
    
    // Moving to kth node from beginning
    int x = k - 1;
    while(x--)
    {
        temp1 = temp1 -> next;
    }
    // Storing the kth node value
    int data1 = temp1 -> val;
    
    // Finding kth node from the end
    int a = count - k;
    
    // Moving to kth node from end
    while(a)
    {
        temp2 = temp2 -> next;
        a--;
    }    
    
    int data2 = temp2 -> val;
    temp2 -> val = data1;
    temp1 -> val = data2;
    
    return head;

}