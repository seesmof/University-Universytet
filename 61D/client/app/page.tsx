import { useState } from "react";

export enum SoilType {
  Sandy = "sandy",
  Clay = "clay",
  Chalky = "chalky",
}

export type Field = {
  id: number;
  name: string;
  area: number;
  soilType: SoilType;
  isIrrigated: boolean;
};

export default function IndexPage() {
  const [data, setData] = useState<Field[]>([]);

  return (
    <>
      <header className="border-b-2 flex justify-between p-3 sticky top-0 z-50">
        <h1>PizzaStore</h1>
      </header>
    </>
  );
}
