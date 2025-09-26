const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

export function vigenereEncrypt(message: string, key: string): string {
  let result = "";

  if (!message || !key) {
    return result;
  }

  message = message.toUpperCase();
  key = key.toUpperCase();

  for (let i = 0; i < message.length; i++) {
    const char = message[i];
    const keyChar = key[i % key.length];

    const charIndex = alphabet.indexOf(char);
    const keyIndex = alphabet.indexOf(keyChar);

    if (charIndex === -1 || keyIndex === -1) {
      result += char;
      continue;
    }

    const encryptedIndex = (charIndex + keyIndex) % alphabet.length;
    const encryptedChar = alphabet[encryptedIndex];
    result += encryptedChar;
  }
  console.log(result);

  return result;
}
