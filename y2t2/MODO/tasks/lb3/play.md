1. Написати й відлагодити програму, що реалізує метод Пауелла.
   - Вибрати початкову точку (можна взяти ліву границю заданого інтервала), величину кроку і параметри збіжності. Реалізувати процедуру одновимірного пошуку точки оптимуму заданої функції, застосувавши метод Пауелла.
2. Знайти мінімум заданої функції за допомогою функції scipy.optimize.minimize_scalar(). Порівняти результати, отримані різними способами.
3. Підготувати та надіслати звіт, вміст якого такий:
   - Сформульована мета роботи.
   - Постановка задачі згідно варіанту.
   - Текст програми та результати її роботи.
   - Аналіз отриманих результатів і висновки.
   - Відповіді на 3 контрольні запитання.

---

Розробити программну реалізацію методу пошуку оптимуму з використанням квадратичної апроксимації й точкового оцінювання.

- Написати й відлагодити програму, що реалізує метод Пауелла.
- Вибрати початкову точку $x_0$, величину кроку $\Delta$ і параметри збіжності $\varepsilon_1$ і $\varepsilon_2$.
- Реалізувати процедуру одновимірного пошуку точки оптимуму заданої функції, застосувавши метод послідовного оцінювання з використанням квадратичної апроксимації (метод Пауелла).
- Знайти мінімум заданої функції за допомогою функції scipy.optimize.minimize_scalar(). Порівняти результати, отримані різними способами.

---

- $w_1$ - starting point
- $\Delta w$ - selected step size along the w-axis

1. Calculate $w_2=w_1+\Delta w$
2. Calculate $f(w_1) \space and \space f(w_2)$
3. If $f(w_1) > f(w_2)$, then put $w_3=w_1+2\Delta w$, else put $w_3=w_1-\Delta w$
4. Calculate $f(w_3)$ and find $F_{min}=min(f_1,f_2,f_3), w_{min}=w_j$, step is $F_{min}$
5. Taking three points $w_1, w_2, w_3$ calculate them, using formula for quadratic approximation
6. Checking if function can end
   1. Is difference $F_{min}-f(w')$ small enough?
   2. Is difference $w_{min}-w'$ small enough?
   - if both conditions are true, stop, otherwise continue
7. Choose the "best" point from $w_{min} or w'$ and two points on both sides from it. Mark those points in the order as they are and go to step 4

the function is $(x-2)^2$
