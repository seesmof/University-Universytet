export const ALPHABETS = {
  EN: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
  UK: "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ",
};

const vigenereCipher = (
  text: string,
  key: string,
  toDecrypt: boolean = false,
  alphabet: string
) => {
  const keyPattern = new RegExp(`[^${alphabet}]`, "gi");
  const clearKey = key.replace(keyPattern, "");
};
