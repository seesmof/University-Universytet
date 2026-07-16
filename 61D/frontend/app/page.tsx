"use client";

import { FormEvent, useState } from "react";

const API_URL = "https://open-bible-api.vercel.app";

export default function IndexPage() {
  const [reference, setReference] = useState<string>("");
  const [text, setText] = useState<string>("");

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();

    const response = await fetch(`${API_URL}/${reference}`);
    const data = await response.json();
    setText(data.verse);
  };

  return (
    <div className="max-w-3xl mx-auto w-full p-3">
      <form className="flex gap-3" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Please enter a Bible reference..."
          className="p-3 border rounded-md flex-1"
          value={reference}
          onChange={(e) => setReference(e.target.value)}
        />
        <button
          className="cursor-pointer hover:bg-sky-600 bg-sky-500 font-bold text-white p-3 rounded-md"
          type="submit"
        >
          Search
        </button>
      </form>
      <div className="border p-3 rounded-md mt-3">
        {!text ? <p>Waiting for the text...</p> : <p>{text}</p>}
      </div>
    </div>
  );
}
