export const main = () => {
  const data: number[] = [1, 2, 3, 4, 5];
  const sum: number = data.reduce((sum, item) => sum + item, 0);
  console.log(sum);
};

main();
