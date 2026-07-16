"use client";

import { useEffect, useState } from "react";
import { User } from "./api/users/route";

export default function IndexPage() {
  const [data, setData] = useState<User[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(false);

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);

      const response = await fetch("/api/users");

      if (!response.ok) throw new Error("Failed to fetch users.");

      const data = await response.json();
      setData(data);

      setIsLoading(false);
    };
    fetchData();
  }, []);

  if (isLoading)
    return (
      <div className="p-3">
        <p>Waiting for the data...</p>
      </div>
    );

  if (!isLoading && data)
    return (
      <div className="p-3 grid grid-cols-1 md:grid-cols-3 gap-3">
        {data.map((user, index) => (
          <div
            className="rounded-md border p-3 gap-1 flex flex-col"
            key={index}
          >
            <h2>{user.name}</h2>
            <em>{user.email}</em>
            <p>{user.age}</p>
          </div>
        ))}
      </div>
    );
}
