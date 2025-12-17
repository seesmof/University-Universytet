"use client";

import { loggedIn } from "@/data/user";
import { redirect } from "next/navigation";

export default function Home() {
  if (!loggedIn) {
    redirect("/login");
  }

  return (
    <>
      <h1>Jesus is LORD</h1>
    </>
  );
}
