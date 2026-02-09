"use client";

import montgomery from "@/helper/montgomery";
import Link from "next/link";
import { FormEvent, useState } from "react";

export default function Home() {
  const [result, setResult] = useState<bigint>(0n);

  const [base, setBase] = useState<bigint>(0n);
  const [exponent, setExponent] = useState<bigint>(0n);
  const [modulus, setModulus] = useState<bigint>(0n);

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();

    setResult(montgomery(base, exponent, modulus));
  };

  return (
    <div className="min-h-screen bg-linear-to-br to-sky-50 p-3 flex flex-col gap-3 items-center justify-center">
      <section className="bg-white rounded-md p-3 flex flex-col w-64 shadow">
        <h1 className="font-bold">TR2. Montgomery Descent</h1>
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
              value={base.toString()}
              onChange={(e) => setBase(BigInt(e.target.value))}
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
              value={exponent.toString()}
              onChange={(e) => setExponent(BigInt(e.target.value))}
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
              value={modulus.toString()}
              onChange={(e) => setModulus(BigInt(e.target.value))}
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
            value={result.toString()}
            readOnly
            className="textarea resize-none"
          ></textarea>
        </div>
      </section>

      <nav className="bg-white rounded-md p-3 flex flex-row w-64 shadow justify-between">
        <Link className="hover:underline underline-offset-4" href={"/"}>
          Binary
        </Link>
        <Link className="underline underline-offset-4" href={"/mont/"}>
          Montgomery
        </Link>
        <Link className="hover:underline underline-offset-4" href={"/ridge/"}>
          Ridge
        </Link>
      </nav>
    </div>
  );
}
