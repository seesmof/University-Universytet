"use client";

import { useState } from "react";

export default function Home() {
  const [value, setValue] = useState<string>(
    "fn main() {\n  let y: i32 = 30;\n}",
  );
  const [output, setOutput] = useState<string>("");

  return (
    <div className="flex flex-col p-3 md:flex-row gap-3 min-h-screen">
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
        value={output}
      />
      <section className="flex flex-row gap-3 w-full">
        <button className="flex-1 btn">Lexical</button>
        <button className="flex-1 btn">Syntactic</button>
        <button className="flex-1 btn">Semantic</button>
        <button className="flex-1 btn">Run</button>
      </section>
    </div>
  );
}
