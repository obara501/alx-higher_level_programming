#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *pointer1 = list, *pointer2 = list;

	while (pointer1 && pointer2 && pointer2->next)
	{
		pointer1 = pointer1->next;
		pointer2 = pointer2->next->next;
		if (pointer1 == pointer2)
			return (1);
	}

	return (0);
}
