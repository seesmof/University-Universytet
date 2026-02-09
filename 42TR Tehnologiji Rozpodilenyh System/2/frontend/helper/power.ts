export default function modularExponentiation(
  a: bigint,
  n: bigint,
  m: bigint,
): bigint {
  // 1. Якщо n = 1, повертаємо a mod m
  if (n === 1n) {
    return a % m;
  }

  // 2. Визначаємо довжину N та ініціалізуємо змінні
  const binaryN = n.toString(2);
  const N = binaryN.length;
  let y = a % m;

  // 3-5. Цикл від k = N-2 до 0
  for (let k = N - 2; k >= 0; k--) {
    // 4. Квадрування
    y = (y * y) % m;

    // 5. Перевірка i-го біта (зліва направо)
    if ((n >> BigInt(k)) & 1n) {
      y = (y * a) % m;
    }
  }

  // 6-7. Повернення результату
  return y;
}
