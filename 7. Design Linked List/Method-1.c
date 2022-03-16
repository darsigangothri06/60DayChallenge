struct Node {
    int val;
    struct Node *next;
};

typedef struct MyLinkedList{
    struct Node *head;

} MyLinkedList;

struct Node *createNode(int val)
{
    struct Node *newNode = malloc(sizeof(struct Node));
    newNode->next = NULL;
    newNode->val = val;
    return newNode;
}

MyLinkedList* myLinkedListCreate() {
    MyLinkedList *obj = malloc(sizeof(MyLinkedList));
    obj->head = NULL;
    return obj;
}

int myLinkedListGet(MyLinkedList* obj, int index) {
    struct Node *current = obj->head;
    if(index == 0 && current)
        return current->val;
    else if(index == 0 && !current)
        return -1;
    else
    {
        for(int i = 0; i<index; i++)
        {
            if(current->next)
                current = current->next;
            else
                return -1;
        }
        return current->val;
    }
}

void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    if(obj->head == NULL)
        obj->head = createNode(val);
    else
    {
        struct Node *temp = obj->head;
        obj->head = createNode(val);
        obj->head->next = temp;
    }
}

void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    struct Node *current;

    if(!obj->head)
        myLinkedListAddAtHead(obj,val);
    else
    {
        current = obj->head;
        while(current->next != NULL)
        {
            current = current->next;
        }
        current->next = createNode(val);
    }
}

void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    struct Node *current = obj->head;
    struct Node *temp;
    if(index == 0)
        myLinkedListAddAtHead(obj,val);

    else if(index > 0 && current)
    {
        for(int i = 1;i<index;i++)
        {
            if(current->next)
                current = current->next;
            else
                return;
        }
        temp = current->next;
        current->next = createNode(val);
        current = current->next;
        current->next = temp;
    }
    else
        return;
}

void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    struct Node *current = obj->head;
    struct Node *deleteNode;

   if(index == 0 && current->next)
    {
        obj->head = current->next;
        free(current);
    }
    else if(index == 0 && !current->next)
    {
        obj->head = NULL;
    }

    else if(current->next)
    {
        for(int i = 1;i < index; i++)
        {
            if(current->next->next)
                current = current->next;
            else
                return;
        }
        deleteNode = current->next;
        current->next = deleteNode->next;
        free(deleteNode);
    }
}

void myLinkedListFree(MyLinkedList* obj) {
    struct Node *temp = obj->head;
    struct Node *next;
    if(temp && temp->next)
    {
        next = temp->next;
        free(temp);
        while(next->next)
        {
            temp = next;
            next = next->next;
            free(temp);
        }
        free(next);
    }
    else if(temp)
    {
        free(temp);
    }
    else
        return;
}

/**
 * Your MyLinkedList struct will be instantiated and called as such:
 * MyLinkedList* obj = myLinkedListCreate();
 * int param_1 = myLinkedListGet(obj, index);
 
 * myLinkedListAddAtHead(obj, val);
 
 * myLinkedListAddAtTail(obj, val);
 
 * myLinkedListAddAtIndex(obj, index, val);
 
 * myLinkedListDeleteAtIndex(obj, index);
 
 * myLinkedListFree(obj);
*/
