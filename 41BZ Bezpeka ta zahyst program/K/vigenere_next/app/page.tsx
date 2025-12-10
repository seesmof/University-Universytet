"use client";

import { useState } from "react";

export default function Home() {
  const [text, setText] = useState("");
  const [key, setKey] = useState("");
  const [output, setOutput] = useState("");

  const baseUrl = "http://127.0.0.1:42248";
  const handleEncrypt = async () => {
    const url = `${baseUrl}/encrypt/?text=${text}&key=${key}`;
    const result = await (await fetch(url)).text();
    setOutput(result);
  };
  const handleDecrypt = async () => {
    const url = `${baseUrl}/decrypt/?text=${text}&key=${key}`;
    const result = await (await fetch(url)).text();
    setOutput(result);
    console.log(key);
  };
  const handlePaste = async () => {
    const data = await navigator.clipboard.readText();
    setText(data);
  };

  const copyResult = () => {
    setText(output);
  };

  const INPUT_CLASSES =
    "outline-2 rounded-md outline-sky-300 focus:outline-sky-500 px-2";
  const BUTTON_CLASSES =
    "bg-sky-50 p-1 hover:bg-sky-200 w-full rounded-md cursor-pointer";
  const BibleVerse =
    "For God so loved the world that He gave His only begotten Son, that whoever believes in Him should not perish, but have eternal life.";

  return (
    <div className="min-h-screen bg-sky-50 flex gap-3 flex-col items-center justify-center">
      {/* Header */}
      <div className="rounded-md bg-white border-2 border-sky-300 flex p-3 gap-3 w-60">
        <span>🔐</span>
        <h1>
          <a
            href="https://en.wikipedia.org/wiki/Vigenère_cipher"
            className="underline underline-offset-2"
          >
            Vigenere Cipher
          </a>
        </h1>
      </div>

      {/* Main App */}
      <div className="rounded-md bg-white border-2 border-sky-300 flex flex-col p-3 gap-4">
        <button className={BUTTON_CLASSES} onClick={handlePaste}>
          Paste
        </button>
        <div className="flex flex-col gap-1">
          <label htmlFor="givenText">Given text</label>
          <textarea
            name="inputText"
            id="inputText"
            className={`${INPUT_CLASSES} resize-none`}
            rows={3}
            placeholder="For example, Some text..."
            value={text}
            onChange={(e) => setText(e.target.value)}
          ></textarea>
        </div>

        <div className="flex flex-col gap-1">
          <label htmlFor="keyInput">Key</label>
          <input
            type="text"
            id="keyInput"
            className={INPUT_CLASSES}
            placeholder="For example, GOD"
            value={key}
            onChange={(e) => setKey(e.target.value.toUpperCase())}
          />
        </div>

        <div className="flex flex-row gap-3" hidden={!text || !key}>
          <button className={BUTTON_CLASSES} onClick={handleEncrypt}>
            Encrypt
          </button>
          <button className={BUTTON_CLASSES} onClick={handleDecrypt}>
            Decrypt
          </button>
        </div>

        <div className="flex flex-col gap-2">
          <textarea
            name="ciphetOutput"
            id="ciphetOutput"
            className={`${INPUT_CLASSES} resize-none`}
            rows={3}
            placeholder="Output will be here..."
            value={output}
            readOnly
            onClick={() => navigator.clipboard.writeText(output)}
          ></textarea>
          <div className="flex flex-row justify-end gap-2">
            <button
              className="bg-sky-50 rounded-md self-end w-fit py-1 px-2"
              onClick={copyResult}
            >
              Reverse
            </button>
            <button
              className="bg-sky-50 rounded-md self-end w-fit py-1 px-2"
              onClick={() => navigator.clipboard.writeText(output)}
            >
              Copy
            </button>
          </div>
        </div>
      </div>

      {/* Bible */}
      <div className="rounded-md bg-white border-2 border-sky-300 flex flex-col p-3 w-60">
        <span
          className="italic text-justify cursor-copy"
          onClick={() => navigator.clipboard.writeText(BibleVerse)}
        >
          {BibleVerse}
        </span>
        <span className="self-end">
          (
          <a
            className="underline underline-offset-2"
            href="https://www.biblegateway.com/passage/?search=John%203%3A16&version=UKR"
          >
            John 3:16
          </a>
          )
        </span>
      </div>
    </div>
  );
}
