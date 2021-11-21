#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
/**
 * listint_len - return number of elements in linked list
 * @h: head of list
 * Return: number of node
 */
size_t listint_len(const listint_t *h)
{
	size_t i = 0;

	while (h)
	{
		h = h->next;
		i++;
	}
	return (i);
}

/**
 * getarray - returns array from linked list
 * @head: head of list
 * Return: array of ints
 */
int *getarray(listint_t *head)
{
	size_t len = listint_len(head), i;
	int *arr = malloc(sizeof(int) * len);

	if (arr == NULL)
		return (NULL);
	for (i = 0; head != NULL; i++, head = head->next)
		arr[i] = head->n;

	return (arr);
}

/**
 * is_palindrome - checks if the list palindrome
 * @head: head of the list
 * Return: 1 if true, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	size_t len, i;
	int *list;

	if (*head == NULL)
		return (1);

	len = listint_len(*head);
	list = getarray(*head);
	for (i = 0; i < len / 2; i++)
	{
		if (list[i] != list[len - 1 - i])
		{
			free(list);
			return (0);
		}
	}
	free(list);
	return (1);
}
