#include "../lib.h"
using namespace std;

// Варіант 5. Створити динамічний клас Route на основі двозв’язного списку, де кожний елемент типа stop (зупинка). Клас повинен містити наступні операції:
// add_stop() – додавання зупинки;
// len_route() – розрахунок довжини маршруту;
// time_route() – розрахувати час руху.

class Route
{
private:
    class Stop
    {
        friend class Route;
        Stop *next;
        Stop *prev;
    };
};

int main()
{
}