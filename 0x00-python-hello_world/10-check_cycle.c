#include "lists.h"

/**
 * check_cycle - checks if list contains cycle in it
 * @list: singly linked list
 * Return: 1 if true 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;

	for (; head->next != NULL; head = head->next)
		if (head->next == list)
			return (1);
	return (0);
}

