#include <stdio.h>
#include <stdlib.h>

struct Node
{
  int data;
  int priority;
  struct Node* next;
};

struct Node* newNode(int d, int p)
{
  struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
  temp->data = d;
  temp->priority = p;
  temp->next = NULL;

  return temp;
}

int peek(struct Node** head)
{
  return (*head)->data;
}

void pop(struct Node** head)
{
  //struct Node* temp = *head;
  (*head) = (*head)->next;
  //free(temp);
  //*head = *head->next;
}

void push(struct Node** head, int d, int p)
{
  struct Node* new = newNode(d, p);

  while ((*head)->next != NULL&& (*head)->next->priority < p)
  {
    (*head) = (*head)->next;
  }
  new->next = (*head)->next;
  (*head)->next = new;

}

int main()
{
  struct Node* head;
  head = newNode(4,1);
  push(&head, 5, 2);
  /*printf("%d\n", head->data);
  printf("%d\n", head->priority);
  printf("%d\n", peek(&head));
  printf("%d\n", head->next->data);*/
  struct Node* traverse;
  printf("%d\n", peek(&head->next));
  while (traverse->next != NULL)
  {
    printf("%d%d\n", traverse->data, traverse->priority);
    &traverse = traverse->next;
  }
  printf("%d\n", peek(&head));
}
