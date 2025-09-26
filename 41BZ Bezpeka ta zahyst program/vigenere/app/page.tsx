"use client";

import { useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("");
  const [key, setKey] = useState("");
  const [encrypted, setEncrypted] = useState("");

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    fetch("/api/vigenere", {
      method: "POST",
      body: JSON.stringify({ message, key }),
    })
      .then((res) => res.json())
      .then((data) => {
        setEncrypted(data.encrypted);
      });
  };

  return (
    <div className="flex h-screen items-center justify-center bg-linear-to-br to-sky-100">
      <div className="flex w-full max-w-xl flex-col p-3">
        <h2 className="mb-7 border-l-2 border-sky-300 pl-3 text-xl">
          Data for the app
        </h2>
        <form className="flex flex-col gap-7">
          <div className="flex flex-row gap-3">
            <label htmlFor="givenTextInput" className="self-center text-4xl">
              📃
            </label>
            <input
              type="text"
              name="givenText"
              id="givenTextInput"
              placeholder="The text to encrypt..."
              className="w-full rounded-md p-3 outline-2 outline-sky-200 focus:outline-sky-300"
              onChange={(e) => setMessage(e.target.value)}
            />
          </div>
          <div className="flex flex-row gap-3">
            <label htmlFor="keyInput" className="self-center text-4xl">
              🗝️
            </label>
            <input
              type="text"
              name="key"
              id="keyInput"
              placeholder="The key here..."
              className="w-full rounded-md p-3 outline-2 outline-sky-200 focus:outline-sky-300"
              onChange={(e) => setKey(e.target.value)}
            />
          </div>
          <input
            type="submit"
            value="Encrypt"
            className="rounded-md bg-sky-300 p-3 text-sky-50 hover:bg-sky-200 active:bg-sky-200"
          />
        </form>

        <h2 className="my-7 mt-12 border-l-2 border-sky-300 pl-3 text-xl">
          Encryption results
        </h2>
        <div className="flex flex-row gap-3">
          <label htmlFor="keyInput" className="self-center text-4xl">
            🔐
          </label>
          <input
            type="text"
            name="result"
            id="resultOutput"
            placeholder=""
            className="w-full rounded-md p-3 outline-2 outline-sky-200"
            readOnly
          />
        </div>
      </div>
    </div>
  );
}
