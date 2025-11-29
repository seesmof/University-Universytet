### Моделювання системи масового обслуговування зі зворотнім зв'язком. Моделювання багатоканальної системи масового обслуговування

#### Мета робота

Метою роботи є вивчення методів моделювання СМО зі зворотнім зв'язком та багатоканальних СМО на основі використання SIMC

#### Текст першої програми

```cpp
#include "../simc/simc.h"
#include <iostream>
using namespace std;

void one() {
  auto Total_Modeling_Time=40*60;

  auto Assembly_Delay=30;
  auto Assembly_Price=50;
  auto Firing_Delay=8;
  auto Firing_Price=200;

  auto Material_Price=2;
  auto Product_Price=7;

  auto Total_Money=0;
  auto Total_Queue=0;

  pqueue Assembly_Queue;
  pqueue Firing_Queue;
  pstorage Assembly_Storage;
  pstorage Firing_Facility;

  initlist(Total_Modeling_Time);
  initcreate(1, 0);
  newqueue(Assembly_Queue, "\"Assembly Queue\"");
  newqueue(Firing_Queue, "\"Firing Queue\"");
  newstorage(Assembly_Storage, "\"Assembly Storage\"", 3);
  newstorage(Firing_Facility, "\"Firing Facility\"",1);

  while (systime < Total_Modeling_Time) {
    plan();
    switch (sysevent) {
      case 1:
        if (int(systime) % 8*60 == 0) Total_Money-=Firing_Price;
        if (int(systime) % 1*60 == 0) Total_Money-=Assembly_Price;
        inqueue(Assembly_Queue); Total_Queue+=1; break;
      case 2: enter(Assembly_Storage,1); break;
      case 3: outqueue(Assembly_Queue); break;
      case 4: delayt(Assembly_Delay); break;
      case 5: leave(Assembly_Storage,1); break;

      case 6: inqueue(Firing_Queue); Total_Queue+=1; break;
      case 8: enter(Firing_Facility,1); break;
      case 9: outqueue(Firing_Queue); break;
      case 10: delayt(Firing_Delay); break;
      case 11: leave(Firing_Facility,1); Total_Money+=Product_Price-Material_Price; break;

      case 12: next(1); break;
    }
  }

  cout << "Total Money: " << Total_Money << endl << "Optimal Queue: " << Total_Queue << endl << endl;
  printall();
  clear();
  destrs(Assembly_Storage);
  destrs(Firing_Facility);
}

void two() {
  auto Total_Modeling_Time=40*60;

  auto Assembly_Delay=30;
  auto Assembly_Price=50;
  auto Firing_Delay=8;
  auto Firing_Price=200;

  auto Material_Price=2;
  auto Product_Price=7;

  auto Query_Interval=115;
  auto Assembly_Time=335;
  auto Firing_Time=110;

  auto Total_Money=0;
  auto Total_Queue=0;

  auto Total_Assembly_Queue=0;
  auto Total_Firing_Queue=0;
  auto Total_Requests=0;
  auto Maximum_Aseembly_Queue=0;

  pqueue Assembly_Queue;
  pqueue Firing_Queue;
  pstorage Assembly_Storage;
  pstorage Firing_Facility;

  initlist(Total_Modeling_Time);
  initcreate(1, 0);
  newqueue(Assembly_Queue, "\"Assembly Queue\"");
  newqueue(Firing_Queue, "\"Firing Queue\"");
  newstorage(Assembly_Storage, "\"Assembly Storage\"", 3);
  newstorage(Firing_Facility, "\"Firing Facility\"",1);

  while (systime < Total_Modeling_Time) {
    plan();
    Firing_Queue->mq=1;
    switch (sysevent) {
      case 1:
        Total_Requests+=1;
        if (int(systime) % 8*60 == 0) Total_Money-=Firing_Price;
        if (int(systime) % 1*60 == 0) Total_Money-=Assembly_Price;
        Total_Assembly_Queue+=1;
        inqueue(Assembly_Queue); Total_Queue+=1;
        if (Assembly_Queue->lq>Maximum_Aseembly_Queue) Maximum_Aseembly_Queue=Assembly_Queue->lq;
        break;
      case 2: enter(Assembly_Storage,1); break;
      case 3: outqueue(Assembly_Queue); break;
      case 4: delayt(Assembly_Delay); break;
      case 5: leave(Assembly_Storage,1); break;

      case 6: Total_Firing_Queue+=1; inqueue(Firing_Queue); Total_Queue+=1; break;
      case 8: enter(Firing_Facility,1); break;
      case 9: outqueue(Firing_Queue); break;
      case 10: delayt(Firing_Delay); break;
      case 11: leave(Firing_Facility,1); Total_Money+=Product_Price-Material_Price; break;

      case 12: next(1); break;
    }
  }

  auto Average_Assembly_Queue=Total_Assembly_Queue/Total_Requests;
  cout << "Average Assembly Queue: " << Average_Assembly_Queue << endl;
  cout << "Total Requests: " << Total_Requests << endl;
  cout << "Total Assembly Queue: " << Total_Assembly_Queue << endl;
  cout << "Total Firing Queue: " << Total_Firing_Queue << endl;
  cout << "Maximum Assembly Queue: " << Maximum_Aseembly_Queue << endl;
  cout << "Total Money: " << Total_Money << endl << "Optimal Queue: " << Total_Queue << endl << endl;
  printall();
  clear();
  destrs(Assembly_Storage);
  destrs(Firing_Facility);
}

void three() {
  pfacility First_Facility;
  pfacility Second_Facility;

  auto First_Interval=1;
  auto First_Delay=1;
  auto Second_Interval=4;
  auto Second_Delay=5;

  auto Total_Modeling_Time=300;

  initlist(Total_Modeling_Time);
  initcreate(1, 0);
  initcreate(7, 0);
  newfac(First_Facility, "\"First Facility\"");
  newfac(Second_Facility, "\"Second Facility\"");

  while (systime < Total_Modeling_Time) {
    plan();
    switch (sysevent) {
      case 1: create(First_Interval); break;
      case 2: if (Second_Facility->status != facility::seized) wait(8); break;
      case 3: seize(First_Facility); break;
      case 4: delayt(First_Delay); break;
      case 5: outfac(First_Facility); break;
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

int main() {
  one();
  two();
  three();
  return 0;
}
```

#### Висновки

Таким чином, ми вивчили методи моделювання СМО зі зворотнім зв'язком, а також багатоканальні СМО на основі використання SIMC

##### Контрольні Питання

###### Багатоканальні прилади. Множинні типи даних "НАКОПИЧУВАЧ" (багатоканальний прилад)

Накопичувач то є багатоканальний прилад де сам накопичувач може бути звільнений не тим транзактом, яким був зайнятий. То є динамічний об'єкт для моделювання декілької пристроїв.

###### Процедури створення – знищення накопичувача

Створення накопичувачів виконується функцією `newstorage`, а знищення виконується функцією `destrs`.

###### Блокування транзактів

Блокування транзактів здійснюється функцією `void wait(event e)` де e то є номер очікуваної події.