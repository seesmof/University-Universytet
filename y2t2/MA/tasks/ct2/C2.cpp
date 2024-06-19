#include "../simc/simc.h"
#include <iostream>
using namespace std;

void Set_Dynamic_Priority(ptransact Current_Transact) {
  const int Max_Priority=7;
  const int Min_Priority=1;
  Current_Transact->prty=randab(Min_Priority, Max_Priority, v1);
}

void Insert_Custom_List(plistt Custom_List) {
  outtlist(current);
  inlt(Custom_List, trans);
  if (trans->pi[2]>=90) Set_Dynamic_Priority(trans);
  trans->testprty = false;
  if (trans->pi[2]>=90) Custom_List->first = Custom_List->first->sled;
  else Custom_List->first = Custom_List->first->sled->sled;
  trans = NULL;
}

void solve() {
  auto Modeling_Hours=7;
  auto Modeling_Time=Modeling_Hours*60;

  pfacility Machine;
  plistt List;

  initlist(Modeling_Time);
  initcreate(1, 0);

  newfac(Machine, "\"Machine\"");
  newuserlt(List, "\"List\"");

  float First_Delay=20.0;
  float Second_Delay=30.0;
  float Third_Delay=40.0;

  auto Average_Interval=2*60.0;

  while (systime < Modeling_Time) {
    plan();
    switch (sysevent) {
      case 1: create(randpoisson(Average_Interval, v7)); trans->pi[2]+=1; break;
      case 2: if (rand01(v1) >= 0.55) { trans->pi[1] = 1; } else if (rand01(v1) >= 0.30) { trans->pi[1] = 2; } else { trans->pi[1] = 3; } break;
      case 4: Insert_Custom_List(List); outuserlt(List); break;
      case 5: seize(Machine); break;
      case 6: if (trans->pi[1]==1) { delayt(randexp(First_Delay,v1)); } else if (trans->pi[1]==2) { delayt(randexp(Second_Delay,v1)); } else { delayt(randexp(Third_Delay,v1)); } break;
      case 8: outfac(Machine); break;
      case 9: destroy(); break;
    }
  }

  cout << "Modeling finished, praise Jesus Christ our Holy Lord GOD Almighty King of Kings and Lord of Lords" << endl << endl;
  printall();
}

int main() {
  solve();
  return 0;
}
// g++ C2.cpp ../simc/simc.cpp -o C2