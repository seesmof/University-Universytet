### The previously discussed optimisation methods are based on the assumption of unimodality and, in some cases, continuity of the objective function under study. What additional condition is required to implement optimisation methods using derivatives?

The condition required to implement optimisation methods using derivatives is the assumption of differentiability. The derivative of the objective function needs to exist and be continuous at the point of interest in order for these methods to function correctly.

### Describe a search procedure that implements the Newton-Raphson method

The Newton-Raphson method is a search procedure that implements the use of numerical derivatives to find the roots of a function.

The procedure is as follows:

1. Choose an initial guess for the root, x_n.
2. Compute the derivative of the function at x_n, f'(x_n).
3. If f'(x_n) is zero, break the loop.
4. Compute the next approximation for the root, x\_{n+1} = x_n - f(x_n) / f'(x_n).
5. If the change in x from the previous iteration is small, break the loop.
6. Set x*n to x*{n+1} and go to step 2.

The Newton-Raphson method is a powerful method for finding roots of functions and is particularly useful for finding the roots of smooth functions with continuous derivatives.

### Describe a search scheme using the midpoint method (Bolzano search)

The midpoint method, also known as the Bolzano search, is a search scheme that involves repeatedly bisecting the current interval until the root is found.

The procedure is as follows:

1. Choose an initial interval [a, b] that contains the root.
2. Compute the midpoint of the interval, m = (a + b) / 2.
3. If f(m) = 0, break the loop.
4. If the sign of f(a) is different from the sign of f(m), set b = m. Otherwise, set a = m.
5. If the interval has shrunk to within a certain tolerance, break the loop.
6. Set the new midpoint as m and go to step 2.

---

### Розглянуті раніше методи оптимізації засновані на припущенні про унімодальність й у ряді випадків про безперервність досліджуваної цільової функції. Виконання якої додаткової умови необхідно для реалізації методів оптимізації з використанням похідних?

Умовою, необхідною для реалізації методів оптимізації з використанням похідних, є припущення про диференційованість. Похідна цільової функції повинна існувати і бути неперервною в точці, що нас цікавить, аби ці методи працювали коректно.

### Опишіть пошукову процедуру, що реалізує метод Нъютона-Рафсона

Метод Ньютона-Рафсона - це процедура пошуку, яка реалізує використання числових похідних для знаходження коренів функції.

Процедура виглядає наступним чином:

1. Вибираємо початкове значення кореня $x_n$.
2. Обчислити похідну функції в точці $x_n, f'(x_n)$.
3. Якщо $f'(x_n)$ дорівнює нулю, завершити цикл.
4. Обчислити наступне наближення для кореня, $x_{n+1} = x_n - f(x_n) / f'(x_n)$.
5. Якщо зміна $x$ від попередньої ітерації мала, то завершити цикл.
6. Встановити $x_n$ у значення $x_{n+1}$ і перейти до кроку 2.

### Опишіть схему пошуку з використанням методу середньої точки (пошуку Больцано)

Метод середньої точки, також відомий як пошук Больцано, - це алгоритм пошуку, який передбачає багаторазове розбиття поточного інтервалу на частини, поки не буде знайдено корінь.

Процедура виглядає наступним чином:

1. Вибрати початковий інтервал [a, b], який містить корінь.
2. Обчислити медіану інтервалу, m = (a + b) / 2.
3. Якщо f(m) = 0, то завершити цикл.
4. Якщо знак f(a) відрізняється від знаку f(m), то встановити b = m. Інакше встановити a = m.
5. Якщо інтервал скоротився до певного допустимого значення, завершити роботу циклу.
6. Встановити нову медіану як m і перейти до кроку 2.
