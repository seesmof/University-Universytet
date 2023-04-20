#include <stdio.h>
#include <conio.h>
char lname[20], fname[15];
int n, god_rogd;
int main()
{
    clrscr();
    puts("Inser last name, first name, year of birth: ")
    puts("then press enter")
    n = scanf("%s %s %d", lname, fname, &god_rogd);
    printf("%d positions are inserted: %s %s %d\n", n, lname, fname, god_rogd);
    return 0;
}