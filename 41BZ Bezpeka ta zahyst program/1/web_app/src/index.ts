const alphabet: string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

function vigenereEncrypt(text: string, key: string): string {
  let result: string = "";
  const upperText = text.toUpperCase();
  const upperKey = key.toUpperCase();

  for (let i = 0; i < upperText.length; i++) {
    const char: string = upperText.charAt(i);
    const keyChar: string = upperKey.charAt(i % upperKey.length);

    const charIndex: number = alphabet.indexOf(char);
    const keyIndex: number = alphabet.indexOf(keyChar);

    if (charIndex === -1 || keyIndex === -1) {
      result += char;
      continue;
    }

    const encryptedIndex: number = (charIndex + keyIndex) % alphabet.length;
    result += alphabet.charAt(encryptedIndex);
  }

  return result;
}

const form = document.getElementById("cipherForm") as HTMLFormElement;
const output = document.getElementById("encryptedText") as HTMLInputElement;

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const text: string = (
    document.getElementById("givenText") as HTMLInputElement
  ).value;
  const key: string = (document.getElementById("key") as HTMLInputElement)
    .value;
  output.value = vigenereEncrypt(text, key);
});
