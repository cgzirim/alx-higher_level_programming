#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: A singly-linked list.
 *
 * Return: If there's no cycle - 0.
 *         If there's a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	if (list == NULL || list->next == NULL)
		return (0);

	listint_t *head = list;

	while (list)
	{
		list = list->next;

		if (head == list)
			return (1);
	}

	return (0);
}
