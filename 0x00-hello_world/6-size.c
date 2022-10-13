#include <stdio.h>
/**
 * main - Entry point
 *
 * this program prints "Programming is like building a multilingual puzzle"
 * Return: Alwayes 0 (success)
 */
int main(void)
{
	char c;
	int i;
	long li;
	long long int lli;
	float f;

	printf("size of a char: %d byte(s)\n", sizeof(c));
	printf("Size of an int: %d byte(s)\n", sizeof(i));
	printf("Size of a long int: %d byte(s)\n", sizeof(li));
	printf("Size of a long long int: %d byte(s)\n", sizeof(lli));
	printf("Size of a float: %d byte(s)\n", sizeof(f));
	return (0);
}
