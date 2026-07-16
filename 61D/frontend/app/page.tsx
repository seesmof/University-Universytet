"use client";

import { useEffect, useState } from "react";
import { User } from "./api/users/route";

export default function IndexPage() {
  const [data, setData] = useState<User[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("/api/users");
      console.log(response);
      const data = await response.json();
      setData(data);
    };
    fetchData();
  }, []);

  return <p>Waiting for the data...</p>;
}
