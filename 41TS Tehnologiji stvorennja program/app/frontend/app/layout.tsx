import type { Metadata } from "next";
import "./globals.css";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Shop",
  description: "",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={"antialiased"}>
        <nav className="rounded-md p-3 outline-2 m-3 flex justify-between items-center">
          <Link
            href="/"
            className="font-medium hover:underline underline-offset-2"
          >
            FoodOrder
          </Link>
          <Link
            href="/cart"
            className="bg-sky-500 text-sky-50 px-3 py-0.5 rounded-md"
          >
            Cart
          </Link>
        </nav>
        {children}
      </body>
    </html>
  );
}
