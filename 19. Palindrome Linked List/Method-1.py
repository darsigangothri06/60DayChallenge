int a[100001];
int i, j, k, temp;
i = 0;
while(head != NULL){
    a[i++] = head -> val;
    head = head -> next;
}
i--;
for(j=0; j <= i/2; j++){
    if(a[j] != a[i-j]){
        return false;
    }
}
return true;