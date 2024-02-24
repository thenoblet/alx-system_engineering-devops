#include <stdio.h>
#include <unistd.h>
/**
* infinite_while - Infinite loop.
* Return: Nothing, is an infinite loop :P.
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
* main - Entry point.
* Return: Always 0.
*/
int main(void)
{
	pid_t zombie;
	short i;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
	}
	infinite_while();
	return (0);
}
