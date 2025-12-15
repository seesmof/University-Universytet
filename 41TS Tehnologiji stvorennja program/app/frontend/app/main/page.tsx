"use client";

import Image from "next/image";

// Sushi type
type Sushi = {
  id: number;
  name: string;
  price: number;
  image: string;
};

export default function Main() {
  const products: Sushi[] = [
    {
      id: 1,
      name: "Nuggets Bowl",
      price: 10,
      image: "bowl-nuggets.jpg",
    },
    {
      id: 2,
      name: "Potato Bowl",
      price: 10,
      image: "bowl-potato.jpg",
    },
    {
      id: 3,
      name: "Rice Bowl",
      price: 10,
      image: "bowl-two.jpg",
    },
    {
      id: 4,
      name: "Nuggets Plate",
      price: 8,
      image: "nuggets.jpg",
    },
    {
      id: 5,
      name: "Sticks Plate",
      price: 8,
      image: "sticks.jpg",
    },
    {
      id: 6,
      name: "Sushi Coral",
      price: 12,
      image: "sushi-coral.jpg",
    },
    {
      id: 7,
      name: "Sushi Green",
      price: 12,
      image: "sushi-green.jpg",
    },
    {
      id: 8,
      name: "Sushi White",
      price: 12,
      image: "sushi-white.jpg",
    },
  ];

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
                onClick={() =>
                  sessionStorage.setItem("product", product.id.toString())
                }
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
