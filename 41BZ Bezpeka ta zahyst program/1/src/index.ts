const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const form = document.getElementById("cipherForm") as HTMLFormElement;
const output = document.getElementById("output") as HTMLInputElement;

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const text = (form.elements.namedItem("text") as HTMLInputElement).value;
  const key = (form.elements.namedItem("key") as HTMLInputElement).value;

  const encrypted = encrypt(text, key);
  output.value = encrypted;
});

function encrypt(text: string, key: string): string {
  let result = "";
  const upperText = text.toUpperCase();
  const upperKey = key.toUpperCase();

  for (let i = 0; i < text.length; i++) {
    const char = upperText.charAt(i);
    const keyChar = upperKey.charAt(i % key.length);

    const charIndex = alphabet.indexOf(char);
    const keyIndex = alphabet.indexOf(keyChar);

    if (charIndex === -1 || keyIndex === -1) {
      result += char;
      continue;
    }

    const encryptedIndex = (charIndex + keyIndex) % alphabet.length;
    result += alphabet[encryptedIndex];
  }

  return result;
}
