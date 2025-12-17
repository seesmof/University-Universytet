export type Product = {
  id: number;
  name: string;
  price: number;
  image: string;
};

export const products: Product[] = [
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
