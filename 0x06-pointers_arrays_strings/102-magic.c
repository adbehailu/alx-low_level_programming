#include <stdio.h>

/**
 * main - Entry point
 * decription: 'the program description
 * Return: Always 0 (Success)
 * write your line of code here...
 * Remember:
 * - you are not allowed to use a
 */

int main(void)
{
	int n;
	int a[5];
	int *p;

	a[2] = 1024;
	p = &n;
	*(p + 5) = 98;
	printf("a[2] = %d\n", a[2]);
	return (0);
}
