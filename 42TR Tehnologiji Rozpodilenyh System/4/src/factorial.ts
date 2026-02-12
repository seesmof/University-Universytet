/**
 * @function factorial
 * @description Calculate a factorial of a number.
 * @param {number} num - A number.
 * @returns {number} - The factorial.
 * @see https://en.wikipedia.org/wiki/factorial
 * @author https://github.com/TheAlgorithms/TypeScript/blob/master/maths/factorial.ts
 * @example factorial(0) = 1
 * @example factorial(3) = 6
 */

export const factorial = (num: number): number => {
  if (num < 0 || !Number.isInteger(num))
    throw new Error("only natural numbers are supported ");

  return num === 0 ? 1 : num * factorial(num - 1);
};

console.log(factorial(0));
console.log(factorial(3));
