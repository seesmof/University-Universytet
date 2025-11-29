#include "../simc/simc.h"
#include <iostream>
using namespace std;

void one() {
  auto Total_Modeling_Time = 8*60*60;
  auto Last_Time = NULL;

  auto Interval_Min=300-20;
  auto Interval_Max=300+20;

  auto First_Delay_Min=100-20;
  auto First_Delay_Max=100+20;

  auto Second_Delay_Min=110-25;
  auto Second_Delay_Max=110+25;

  /*
  first: first, second
  second: first, second
  third: first
  */

  pfacility First_Worker;
  pfacility Second_Worker;

  signalp Signal;
  phistogram Interval_Graphics;

  initlist(Total_Modeling_Time);
  initcreate(1, 0);

  newfac(First_Worker, "\"First Worker\"");
  newfac(Second_Worker, "\"Second Worker\"");
  newhist(Interval_Graphics, 177,277, 10, true, "\"Intervals\"");

  while (systime < Total_Modeling_Time) {
    plan();
    switch (sysevent) {
      case 1: create(randab(Interval_Min,Interval_Max,v1)); Last_Time = systime; break;
      case 2: split(1,8); break;
      case 3: seize(First_Worker); break;
      case 4: delayt(randab(First_Delay_Min,First_Delay_Max,v1)); break;
      case 5: outfac(First_Worker); break;
      case 6: if (Second_Worker->status == facility::seized) accept(Signal); else send(Signal); break;
      case 7: next(13); break;
      case 8: seize(Second_Worker); break;
      case 9: delayt(randab(Second_Delay_Min,Second_Delay_Max,v1)); break;
      case 10: outfac(Second_Worker); break;
      case 11: if (First_Worker->status == facility::seized) accept(Signal); else send(Signal); break;
      case 12: next(18); break;
      case 13: seize(First_Worker); break;
      case 14: delayt(randab(First_Delay_Min,First_Delay_Max,v1)); break;
      case 15: outfac(First_Worker); break;
      case 16: if (Second_Worker->status == facility::seized) accept(Signal); else send(Signal); break;
      case 17: next(22); break;
      case 18: seize(Second_Worker); break;
      case 19: delayt(randab(Second_Delay_Min,Second_Delay_Max,v1)); break;
      case 20: outfac(Second_Worker); break;
      case 21: if (First_Worker->status == facility::seized) accept(Signal); else send(Signal); break;
      case 22: assemble(2); break;
      case 23: tabulate(Interval_Graphics, systime - Last_Time); destroy(); break;
    }
  }
  printall();
  cout << "Modeling finished, glory to Jesus Christ our Holy Lord GOD Almighty King of Kings and Lord of Lords" << endl << endl;
}

void two() {
  auto Patient_Interval_Min=6-1;
  auto Patient_Interval_Max=6+1;

  auto Doctor_Interval_Min=7-2;
  auto Doctor_Interval_Max=7+2;
  
  auto Total_Modeling_Time = 3*60;
  auto Total_Patients = 0;

  pfacility Doctors_Office;
  plistt Doctors_Queue;

  initlist(Total_Modeling_Time);
  initcreate(1, 0);

  newfac(Doctors_Office, "\"Doctors Office\"");
  newuserlt(Doctors_Queue, "\"Doctor Queue\"");

  while (systime < Total_Modeling_Time) {
    plan();
    switch (sysevent) {
      case 1: create(randab(Patient_Interval_Min, Patient_Interval_Max, v1)); break;
      case 2: trans->testprty = false; inlfifo(Doctors_Queue); outuserlt(Doctors_Queue); break;
      case 3: seize(Doctors_Office); break;
      case 4: delayt(randab(Doctor_Interval_Min, Doctor_Interval_Max, v1)); break;
      case 5: outfac(Doctors_Office); break;
      case 6: Total_Patients+=1; destroy(); break;
    }
  }

  cout << "Total Patients: " << Total_Patients << endl;
  printall();
}

int main()
{
  one();
  two();
  return 0;
}
// g++ Five_General.cpp ../simc/simc.cpp -o Five_General