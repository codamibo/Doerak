#include <stdio.h>

int str_len(char *string)
{
	int		i;

	i = 0;
	while (string[i])
		i++;
	return (i);
}

int	 main(int argc, char **argv)
{
	int		a[7] = {0, 1, 23, 4, 234, 5, 6};
	char	b = 'c';
	char	*string = "hoi";
	int		i;

	printf("%i\n", str_len(string));
	//comment
	/*
	lange comment
	*/
	i = 0;
	for (i; i < 10; ++i)
	{
		printf("%i\n", i);
	}
	if (argc > 2)
	{
		printf("%s\n", argv[1]);
		printf("%s\n", argv[2]);
	}
	return (0);
}
