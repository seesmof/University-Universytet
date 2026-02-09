export const powerModular = (a: number, n: number, m: number): number => {
  /*
   * Обчислює (a^e)%m за допомогою бінарного методу.
   *
   * @param a: основа, base
   * @param n: ступінь, exponent
   * @param m: модуль, modulus
   */

  if (m === 1) return 0;
  let result: number = 1;
  a = a % m;

  while (n > 0) {
    if (n % 2 === 1) result = (result * a) % m;
    n = Math.floor(n / 2);
    a = (a * a) % m;
  }

  return result;
};
