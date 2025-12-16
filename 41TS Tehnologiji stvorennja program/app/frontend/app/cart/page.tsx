"use client";

import { cartProducts } from "@/data/cart";
import Image from "next/image";

export default function Cart() {
  const removeItem = (id: number) => {
    cartProducts.filter((p) => p.id !== id);
  };

  return (
    <div className="p-3 flex flex-col">
      {cartProducts.map((product) => (
        <div
          key={product.id}
          className="outline-2 p-3 rounded-md flex flex-col gap-3 md:flex-row"
        >
          <Image
            src={`/${product.image}`}
            alt={product.name}
            width={500}
            height={500}
            className="w-full rounded-md max-w-1/2"
          />
          <div className="flex flex-col w-full">
            <h2 className="mt-2 md:mt-0 text-lg">{product.name}</h2>
            <div className="fle"></div>
            <div className="flex flex-row justify-between mt-2 w-full">
              <p className="">${product.price}</p>
              <button
                className="w-min bg-sky-500 text-sky-50 rounded-md px-3 py-1 cursor-pointer"
                onClick={() => removeItem(product.id)}
              >
                Buy
              </button>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}
