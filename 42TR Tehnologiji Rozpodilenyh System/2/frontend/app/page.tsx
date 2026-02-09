"use client";

import { powerModular } from "@/helper/main";
import { FormEvent, useState } from "react";

export default function Home() {
  const [result, setResult] = useState(0);

  const [base, setBase] = useState(0);
  const [exponent, setExponent] = useState(0);
  const [modulus, setModulus] = useState(0);

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();

    setResult(powerModular(base, exponent, modulus));
  };

  return (
    <div className="min-h-screen bg-linear-to-br to-sky-50 p-3 flex flex-col gap-3 items-center justify-center">
      <section className="bg-white rounded-md p-3 flex flex-col w-64 shadow">
        <h1 className="font-bold">TR2. Binary Exponent</h1>
      </section>
      <section className="bg-white rounded-md p-3 flex flex-col w-64 shadow">
        <form className="flex flex-col gap-3" onSubmit={handleSubmit}>
          <div className="flex flex-col gap-1">
            <label htmlFor="baseInput" className="label">
              Base
            </label>
            <input
              id="baseInput"
              className="input"
              type="text"
              value={base}
              onChange={(e) => setBase(+e.target.value)}
            />
          </div>

          <div className="flex flex-col gap-1">
            <label htmlFor="exponentInput" className="label">
              Exponent
            </label>
            <input
              id="exponentInput"
              className="input"
              type="text"
              value={exponent}
              onChange={(e) => setExponent(+e.target.value)}
            />
          </div>

          <div className="flex flex-col gap-1">
            <label htmlFor="modulusInput" className="label">
              Modulus
            </label>
            <input
              id="modulusInput"
              className="input"
              type="text"
              value={modulus}
              onChange={(e) => setModulus(+e.target.value)}
            />
          </div>

          <button className="btn">Submit</button>
        </form>
      </section>

      <section className="bg-white rounded-md p-3 flex flex-col w-64 shadow">
        <div className="flex flex-col gap-1">
          <label htmlFor="output" className="label">
            Result
          </label>
          <textarea
            name="output"
            id="output"
            value={result}
            readOnly
            className="textarea resize-none"
          ></textarea>
        </div>
      </section>
    </div>
  );
}
