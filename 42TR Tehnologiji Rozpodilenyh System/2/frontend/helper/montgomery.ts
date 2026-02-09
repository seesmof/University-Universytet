/**
 * @param a base,
 * @param n exponent,
 * @param m modulus.
 */

export default function montgomery(
  n: number | bigint,
  a: number | bigint,
  m: number | bigint,
): bigint {
  // 0. Підготовка: отримуємо двійкове представлення n
  const binaryN = n.toString(2);
  const N = binaryN.length;

  // 0.1 Перетворення змінних на тип BigInt
  n = BigInt(n);
  a = BigInt(a);
  m = BigInt(m);

  // 1. Ініціалізація
  // y1 = a mod m, y2 = a^2 mod m
  let y1 = a % m;
  let y2 = (a * a) % m;

  // 2. Цикл від k = N-2 до 0
  for (let k = N - 2; k >= 0; k--) {
    // Перевіряємо i-й біт показника n
    const bit = (n >> BigInt(k)) & 1n;

    if (bit === 1n) {
      // Якщо i-й біт дорівнює 1:
      y1 = (y1 * y2) % m;
      y2 = (y2 * y2) % m;
    } else {
      // Якщо i-й біт дорівнює 0 (блок "Інакше"):
      y2 = (y1 * y2) % m;
      y1 = (y1 * y1) % m;
    }
  }

  // 3. Повернення результату
  return y1;
}
