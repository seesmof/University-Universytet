import data from "@/data/data.json";

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
  return (
    <div className="min-h-screen bg-sky-50">
      <div className="container mx-auto p-3 flex items-center justify-center">
        <div className="bg-white p-3 rounded-md shadow">{data["GEN"][1]}</div>
      </div>
    </div>
  );
}
