#include "../simc/simc.h"
#include <iostream>
using namespace std;

void one() {
  auto Modeling_Hours=40;
  auto Total_Modeling_Time=Modeling_Hours*60;

  auto Assembly_Delay=30;
  auto Firing_Delay=8;

  auto Worker_Hourly_Salary=50;
  auto Firing_Daily_Price=200;
  auto Material_Price=2;
  auto Product_Price=7;

  auto Workers_Min=4;
  auto Workers_Max=6;

  auto Best_Result=0;
  auto Best_Count=0;

  pqueue Assembly_Queue;
  pstorage Assembly_Facility;
  pqueue Firing_Queue;
  pfacility Firing_Facility;

  initlist(Total_Modeling_Time);
  initcreate(1, 0);

  newqueue(Assembly_Queue, "\"Assembly Queue\"");
  newqueue(Firing_Queue, "\"Firing Queue\"");
  newfac(Firing_Facility, "\"Firing Facility\"");

  for (auto Workers_Count=Workers_Min;Workers_Count<=Workers_Max;Workers_Count++) {
    for (auto j=Workers_Min;j<=Workers_Count;j++) initcreate(1,0);
    newstorage(Assembly_Facility, "\"Assembly Facility\"", 3);
    auto Parts_Assembled=0;
    while (systime<Total_Modeling_Time) {
      plan();
      switch (sysevent) {
        case 1: inqueue(Assembly_Queue); break;
        case 2: enter(Assembly_Facility, 1); break;
        case 3: outqueue(Assembly_Queue); break;
        case 4: delayt(Assembly_Delay); break;
        case 5: leave(Assembly_Facility, 1); break;

        case 6: inqueue(Firing_Queue); break;
        case 7: seize(Firing_Facility); break;
        case 8: outqueue(Firing_Queue); break;
        case 9: delayt(Firing_Delay); break;
        case 10: outfac(Firing_Facility); Parts_Assembled+=1; break;
        case 11: next(1); break;
      }
    }
    auto Workers_Salary=Worker_Hourly_Salary*Modeling_Hours*Workers_Count;
    auto Firing_Facility_Cost=Firing_Daily_Price/8*Modeling_Hours;
    auto Materials_Cost=Parts_Assembled*Material_Price;
    auto Parts_Cost=Parts_Assembled*Product_Price;
    auto Total_Expenses=Workers_Salary+Firing_Facility_Cost+Materials_Cost;
    auto Profit=Parts_Cost-Total_Expenses;
    if (abs(Profit)>abs(Best_Result)) { Best_Result=Profit; Best_Count=Workers_Count; }
    cout << "Workers: " << Workers_Count << " Profit: " << Profit << endl;
  }

  cout << "\nBest Count: " << Best_Count << " Best Result: " << Best_Result << endl << endl;
  printall();
}

void two() {
  auto Interval=115;

  auto First_Delay=335;
  auto Second_Delay=110;

  auto Modeling_Hours=1;
  auto Total_Modeling_Time=Modeling_Hours*60*60;

  pqueue First_Queue;
  pqueue Second_Queue;
  pfacility First_Facility;
  pfacility Second_Facility;

  initlist(Total_Modeling_Time);
  initcreate(1, 0);

  newqueue(First_Queue, "\"First Queue\"");
  newqueue(Second_Queue, "\"Second Queue\"");
  newfac(First_Facility, "\"First Facility\"");
  newfac(Second_Facility, "\"Second Facility\"");

  while (systime<Total_Modeling_Time) {
    plan();
    switch (sysevent) {
      case 1: create(Interval); break;
      case 2: cout << "First Queue Length: " << First_Queue->lq << endl; if (Second_Queue->status == queue::empty) next(8); else inqueue(First_Queue); break;
      case 3: seize(First_Facility); break;
      case 4: outqueue(First_Queue); break;
      case 5: delayt(First_Delay); break;
      case 6: outfac(First_Facility); break;
      case 7: destroy(); break;

      case 8: create(Interval); break;
      case 9: cout << "Second Queue Length: " << Second_Queue->lq << endl; Second_Queue->mq=1; inqueue(Second_Queue); break;
      case 10: seize(Second_Facility); break;
      case 11: outqueue(Second_Queue); break;
      case 12: delayt(Second_Delay); break;
      case 13: outfac(Second_Facility); break;
      case 14: destroy(); break;
    }
  }

  cout << "\nFirst Queue Max Length: " << First_Queue->mq << " Average Length: " << First_Queue->lm << endl << endl;
  printall();
}

void three() {
  auto First_Interval=1;
  auto First_Delay=1;

  auto Second_Interval=4;
  auto Second_Delay=5;

  auto Total_Modeling_Time=300;

  // first t can be served only if second facility is seized

  pfacility First_Facility;
  pfacility Second_Facility;

  initlist(Total_Modeling_Time);
  initcreate(1, 0);

  newfac(First_Facility, "\"First Facility\"");
  newfac(Second_Facility, "\"Second Facility\"");

  while (systime<Total_Modeling_Time) {
    plan();
    switch (sysevent) {
      case 1: create(First_Interval); break;
      case 2: if (Second_Facility->status == facility::seized) seize(First_Facility); else next(7); break;
      case 3: delayt(First_Delay); break;
      case 4: outfac(First_Facility); break;
      case 6: destroy(); break;

      case 7: create(Second_Interval); break;
      case 8: seize(Second_Facility); break;
      case 9: delayt(Second_Delay); break;
      case 10: outfac(Second_Facility); break;
      case 11: destroy(); break;
    }
  }

  cout << "Modeling finished, praise Jesus Christ our Holy Lord GOD Almighty" << endl << endl;
  printall();
}

int main()
{
  one();
  two();
  three();
  return 0;
}
// g++ Three_General.cpp ../simc/simc.cpp -o Three_General