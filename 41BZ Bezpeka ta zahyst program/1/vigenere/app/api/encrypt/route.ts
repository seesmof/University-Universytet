import { vigenereProcess } from "@/lib/vigenere";
import { NextResponse } from "next/server";

export async function POST(req: Request) {
  const { message, key } = await req.json();

  if (!message || !key) {
    return new Response("Missing message or key", { status: 400 });
  }

  const encrypted = vigenereProcess(message, key);
  const data = { encrypted };

  return NextResponse.json(data);
}
