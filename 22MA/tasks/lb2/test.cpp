#include "../simc/simc.h"
#include <iostream>
using namespace std;

auto STARTING_TIME = 0;
auto TIME_TO_TAKE_PARTS = 4;
auto TIME_TO_WORK = 480;

auto RED_MASS = 2;
auto RED_INTERVAL = 3;
auto RED_HOLES = 0;

auto HEFTY_RED_MASS = 2.4;
auto HEFTY_RED_INTERVAL = 5;
auto HEFTY_RED_HOLES = 0;

auto GREEN_MASS = 3;
auto GREEN_INTERVAL = 20;
auto GREEN_TEMPERATURE = 85;
auto GREEN_HOLES = 2;

auto DRILLING_MACHINE_DURATION = 15;
auto LATHE_DURATION = 20;
auto DRILLING_MACHINE_NAME = "\"Drilling Machine\"";
auto LATHE_NAME = "\"Lathe\"";

auto TOTAL_WORKING_TIME = 0;
auto TOTAL_DRILLING_MACHINE_TIME = 0;
auto TOTAL_LATHE_TIME = 0;
auto TOTAL_HOLES = 0;

void model()
{
  pstorage drillingMachine;
  pstorage lathe;

  initlist(TIME_TO_WORK);
  // red drill
  initcreate(1, STARTING_TIME);
  // hefty red drill
  initcreate(4, STARTING_TIME);
  // green lathe
  initcreate(7, STARTING_TIME);

  newstorage(drillingMachine, DRILLING_MACHINE_NAME, HEFTY_RED_INTERVAL);
  newstorage(lathe, LATHE_NAME, GREEN_INTERVAL);

  const int drillDelay = TIME_TO_TAKE_PARTS + DRILLING_MACHINE_DURATION;
  const int latheDelay = TIME_TO_TAKE_PARTS + LATHE_DURATION;
  cout << "Drilling machine queue: " << endl;

  while (systime < TIME_TO_WORK)
  {
    plan();
    switch (sysevent)
    {
    case 1:
      enter(drillingMachine, 1);
      TOTAL_HOLES += 1;
      cout << "Transact " << trans->nom << " in queue" << endl;
      break;
    case 2:
      delayt(drillDelay);
      TOTAL_WORKING_TIME += drillDelay;
      TOTAL_DRILLING_MACHINE_TIME += drillDelay;
      break;
    case 3:
      leave(drillingMachine, 1);
      cout << "Transact " << trans->nom << " out of queue" << endl;
      break;

    case 4:
      enter(drillingMachine, 1);
      TOTAL_HOLES += 1;
      cout << "Transact " << trans->nom << " in queue" << endl;
      break;
    case 5:
      delayt(drillDelay);
      TOTAL_WORKING_TIME += drillDelay;
      TOTAL_DRILLING_MACHINE_TIME += drillDelay;
      break;
    case 6:
      leave(drillingMachine, 1);
      cout << "Transact " << trans->nom << " out of queue" << endl;
      break;

    case 7:
      enter(lathe, 1);
      cout << "Transact " << trans->nom << " in queue" << endl;
      break;
    case 8:
      delayt(latheDelay);
      TOTAL_WORKING_TIME += latheDelay;
      TOTAL_LATHE_TIME += latheDelay;
      break;
    case 9:
      leave(lathe, 1);
      cout << "Transact " << trans->nom << " out of queue" << endl;
      break;

    case 10:
      next(1);
      cout << endl;
      break;
    }
  }
  printall();
  clear();
  destrs(drillingMachine);
  cout << endl
       << "Modeling finished, praise Jesus Christ our Holy Lord Almighty Living GOD Most High" << endl
       << "  - Total time the machines worked: " << TOTAL_WORKING_TIME << " minutes" << endl
       << "  - Total time the drill worked: " << TOTAL_DRILLING_MACHINE_TIME << " minutes" << endl
       << "  - Total time the lathe worked: " << TOTAL_LATHE_TIME << " minutes" << endl
       << "  - Total number of holes: " << TOTAL_HOLES << endl;
}
int main()
{
  model();
  return 0;
}
// g++ test.cpp ../simc/simc.cpp -o test