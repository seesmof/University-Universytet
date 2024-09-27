#include <stdio.h>

int main()
{
  int index = 0;
  char line[13] = "random text a";
  char result[13] = "JESUS IS KING";

  while (1)
  {
    printf("\r%s", line);
    fflush(stdout);

    line[index] = result[index];
    index = (index + 1) % 13;

    sleep(1);
  }

  return 0;
}