#include "../simc/simc.h"
#include <iostream>
using namespace std;

int main()
{
  pfacility f;
  initlist(100);
  starttrace();
  initcreate(1, 0);
  newfac(f, "Device");
  while (systime < 100)
  {
    plan();
    switch (sysevent)
    {
    case 1:
      create(15);
      break;
    case 2:
      split(11, 7);
      break;
    case 3:
      seize(f);
      break;
    }
  }

  return 0;
}
// g++ gen.cpp ../simc/simc.cpp -o gen