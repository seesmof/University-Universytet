const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
function vigenereEncrypt(text, key) {
  let result = "";
  const upperText = text.toUpperCase();
  const upperKey = key.toUpperCase();
  for (let i = 0; i < upperText.length; i++) {
    const char = upperText.charAt(i);
    const keyChar = upperKey.charAt(i % upperKey.length);
    const charIndex = alphabet.indexOf(char);
    const keyIndex = alphabet.indexOf(keyChar);
    if (charIndex === -1 || keyIndex === -1) {
      result += char;
      continue;
    }
    const encryptedIndex = (charIndex + keyIndex) % alphabet.length;
    result += alphabet.charAt(encryptedIndex);
  }
  return result;
}
const form = document.getElementById("cipherForm");
const output = document.getElementById("encryptedText");
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const text = document.getElementById("givenText").value;
  const key = document.getElementById("key").value;
  output.value = vigenereEncrypt(text, key);
});
//# sourceMappingURL=index.js.map
