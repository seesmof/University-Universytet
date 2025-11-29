#include "../simc/simc.h"
#include <iostream>
using namespace std;

int TOTAL_HOURS = 28800;
int FIRST_INTERVAL = 510;
int FIRST_DURATION = 300;
int SECOND_INTERVAL = 420;
int SECOND_DURATION = 100;

pair<double, double> model(bool givePriorityToYellow = false)
{
  pqueue partsQueue;
  pfacility warehousePerson;
  int totalPeopleInQueue = 0;
  int totalIterations = 0;

  initlist(TOTAL_HOURS);
  initcreate(1, 0);
  initcreate(8, 0);
  newqueue(partsQueue, "\"Orders Order\"");
  newfac(warehousePerson, "\"Warehouse\"");
  while (systime < TOTAL_HOURS)
  {
    plan();
    switch (sysevent)
    {
    case 1:
      create(FIRST_INTERVAL);
      break;
    case 2:
      inqueue(partsQueue);
      trans->prty = 1;
      totalPeopleInQueue += 1;
      break;
    case 3:
      seize(warehousePerson);
      break;
    case 4:
      outqueue(partsQueue);
      totalPeopleInQueue -= 1;
      break;
    case 5:
      delayt(FIRST_DURATION);
      break;
    case 6:
      outfac(warehousePerson);
      break;
    case 7:
      destroy();
      break;

    case 8:
      create(SECOND_INTERVAL);
      break;
    case 9:
      inqueue(partsQueue);
      if (givePriorityToYellow == true)
      {
        trans->prty = 2;
      }
      else
      {
        trans->prty = 1;
      }
      totalPeopleInQueue += 1;
      break;
    case 10:
      seize(warehousePerson);
      break;
    case 11:
      outqueue(partsQueue);
      totalPeopleInQueue -= 1;
      break;
    case 12:
      delayt(SECOND_DURATION);
      break;
    case 13:
      outfac(warehousePerson);
      break;
    case 14:
      destroy();
      break;
    }
    totalIterations += 1;
  }
  printall();
  double averagePeopleInQueue = (double)totalPeopleInQueue / totalIterations;
  double totalMoneyLost = totalPeopleInQueue * 0.25 * FIRST_DURATION + totalPeopleInQueue * 0.25 * SECOND_DURATION;
  return make_pair(averagePeopleInQueue, totalMoneyLost);
}
int main()
{
  pair<double, double> resOne = model(false);
  pair<double, double> resTwo = model(true);

  cout << endl
       << "Average people in queue without prioritization: " << resOne.first << endl;
  cout << "Average people in queue with prioritization: " << resTwo.first << endl;

  cout << "Total money lost without prioritization: " << resOne.second << endl;
  cout << "Total money lost with prioritization: " << resTwo.second << endl;

  return 0;
}
// g++ gen.cpp ../simc/simc.cpp -o gen