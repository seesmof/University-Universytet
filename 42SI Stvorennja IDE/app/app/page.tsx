"use client";

import { useState } from "react";

const parse = (value: string) => {
  const cleanInput = value.replace(/[a-z=]/gi, "");
  const calculatedInput = eval(cleanInput);
  return calculatedInput;
};

export default function Home() {
  const [value, setValue] = useState<string>("32 + 12 - 11");
  const [result, setResult] = useState<string>("");

  const calculateResult = () => {
    const givenResult = parse(value);
    setResult(givenResult);
  };

  return (
    <div className="flex flex-col p-3 gap-3 min-h-screen">
      <textarea
        className="resize-none textarea w-full flex-1 font-mono"
        name="input"
        id="inputArea"
        value={value}
        onChange={(e) => setValue(e.target.value)}
      />
      <textarea
        className="resize-none textarea w-full bg-gray-50"
        name="input"
        id="outputArea"
        readOnly
        rows={7}
        value={result}
        onClick={() => navigator.clipboard.writeText(result)}
      />
      <button className="btn" onClick={calculateResult}>
        Run
      </button>
    </div>
  );
}
