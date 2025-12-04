"use client";

import { useState } from "react";

export default function Home() {
  const [givenText, setGivenText] = useState("");
  const [key, setKey] = useState("");
  const [output, setOutput] = useState("");

  const baseUrl = "http://127.0.0.1:42248";
  const handleEncrypt = async () => {
    let url = `${baseUrl}/encrypt/?text=${givenText}&key=${key}`;
    let result = await (await fetch(url)).text();
    setOutput(result);
  };
  const handleDecrypt = async () => {
    let url = `${baseUrl}/decrypt/?text=${givenText}&key=${key}`;
    let result = await (await fetch(url)).text();
    setOutput(result);
  };

  const inputClasses =
    "outline-2 rounded-md outline-sky-300 focus:outline-sky-500 px-2";
  const BibleVerse =
    "For God so loved the world that He gave His only begotten Son, that whoever believes in Him should not perish, but have eternal life.";

  return (
    <div className="min-h-screen bg-sky-50 flex gap-3 flex-col items-center justify-center">
      {/* Header */}
      <div className="rounded-md bg-white border-2 border-sky-300 flex w-1/4 p-3 gap-3">
        <span>🔐</span>
        <h1>Vigenere Cipherer</h1>
      </div>

      {/* Main App */}
      <div className="rounded-md bg-white border-2 border-sky-300 flex flex-col p-3 gap-4 w-1/4">
        <div className="flex flex-col gap-1">
          <label htmlFor="givenText">Given text</label>
          <input
            type="text"
            id="givenText"
            className={inputClasses}
            placeholder="For example, Some text..."
            value={givenText}
            onChange={(e) => setGivenText(e.target.value)}
          />
        </div>

        <div className="flex flex-col gap-1">
          <label htmlFor="keyInput">Key</label>
          <input
            type="text"
            id="keyInput"
            className={inputClasses}
            placeholder="For example, GOD"
            value={key}
            onChange={(e) => setKey(e.target.value.toUpperCase())}
          />
        </div>

        <div className="flex flex-row gap-3">
          <button
            className="bg-sky-50 p-1 hover:bg-sky-200 w-full rounded-md"
            onClick={handleEncrypt}
          >
            Encrypt
          </button>
          <button
            className="bg-sky-50 p-1 hover:bg-sky-200 w-full rounded-md"
            onClick={handleDecrypt}
          >
            Decrypt
          </button>
        </div>

        <div className="flex flex-col gap-2">
          <textarea
            name="ciphetOutput"
            id="ciphetOutput"
            className={`${inputClasses} resize-none`}
            rows={3}
            placeholder="Output will be here..."
            value={output}
            readOnly
            onClick={(e) => navigator.clipboard.writeText(output)}
          ></textarea>
          <button
            className="bg-sky-50 rounded-md self-end w-fit py-1 px-2"
            onClick={(e) => navigator.clipboard.writeText(output)}
          >
            Copy
          </button>
        </div>
      </div>

      {/* Bible */}
      <div className="rounded-md bg-white border-2 border-sky-300 flex flex-col w-1/4 p-3">
        <span
          className="italic text-justify cursor-copy"
          onClick={(e) => navigator.clipboard.writeText(BibleVerse)}
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
