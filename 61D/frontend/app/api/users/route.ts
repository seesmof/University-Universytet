import { NextResponse } from "next/server";

export interface User {
    name: string,
    email: string,
    age: number,
}

export default async function GET() {
    return NextResponse.json<User[]>([
        { name: "Iva", email: "nipinrid@kolos.cf", age: 46 },
        { name: "Rebecca", email: "guvol@ziinjeb.dm", age: 39 },
        { name: "Maggie", email: "num@sasafaji.su", age: 30 },
        { name: "Eleanor", email: "kica@iz.ly", age: 35 },
        { name: "Charles", email: "ikeveh@ciw.fi", age: 33 },
        { name: "Beulah", email: "nu@defcoki.ir", age: 25 },
        { name: "Adam", email: "bof@ozbenu.hk", age: 39 },
    ])
}