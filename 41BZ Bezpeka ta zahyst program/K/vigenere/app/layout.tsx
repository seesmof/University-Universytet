import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "41K Vigenere",
  description: "Encrypt or decrypt using Vigenere cipher.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={"antialiased"}
      >
        {children}
      </body>
    </html>
  );
}
