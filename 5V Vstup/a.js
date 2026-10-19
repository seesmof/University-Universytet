const totalChapters = 52;
let counter = 1;
for (let index = 1; index < totalChapters; index += 2) {
  console.log(`${counter}. ${index} ${index + 1}`);
  counter++;
}
