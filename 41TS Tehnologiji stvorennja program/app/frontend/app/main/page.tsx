"use client";

import { products } from "@/data/products";
import Image from "next/image";

export default function Main() {
  return (
    <>
      <div className="flex flex-row flex-wrap gap-3 p-3">
        {products.map((product) => (
          <div key={product.id} className="grow p-3 outline-2 rounded-md">
            <Image
              src={`/${product.image}`}
              alt={product.name}
              width={500}
              height={500}
              className="w-full rounded-md"
            />
            <h2 className="mt-2">{product.name}</h2>
            <div className="flex flex-row justify-between mt-2">
              <p className="">${product.price}</p>
              <button
                className="w-min bg-sky-500 text-sky-50 rounded-md px-3 py-1 cursor-pointer"
                onClick={() => {
                  sessionStorage.setItem("cart", [
                    ...sessionStorage.getItem("cart"),
                    product.id,
                  ]);
                  console.log(product.name);
                }}
              >
                +
              </button>
            </div>
          </div>
        ))}
      </div>
    </>
  );
}
