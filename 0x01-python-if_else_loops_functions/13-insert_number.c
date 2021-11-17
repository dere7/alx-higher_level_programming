#include "lists.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - add new node int sorted list
 * @head: head of sorted list to be added
 * @number: integer of node
 * Return: Pointer to newly created node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *h, *prev;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	h = *head;
	if (h->n > number)
	{
		new->next = h;
		*head = new;
	}
	else
		for (prev = h, h = h->next; h->next != NULL; h = h->next, prev = prev->next)
		{
			if (number <= h->n)
			{
				new->next = h;
				prev->next = new;
				break;
			}
		}

	/* if reached end*/
	if (h->next == NULL)
		h->next = new;
	return (new);
}
