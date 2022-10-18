#include "main.h"
/**
 * print_alphabet - print the alphabet in lowercase
 *
 * Return: Alwayes 0 (Success)
 */

void print_alphabet(void)
{
	char alpha;

	for (alhpa = 'a'; alhpa <= 'z'; alpha++)
	{
		_putchar (alpha);
	}
	_putchar('\n');
}
