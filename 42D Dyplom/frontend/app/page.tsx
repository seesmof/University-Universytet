import Link from "next/link";

export default function Home() {
  return (
    <div className="dock">
      <Link href="owned/">
        <span className="dock-label">Owned</span>
      </Link>

      <Link href="/" className="dock-active">
        <span className="dock-label">Store</span>
      </Link>

      <Link href="chat/">
        <span className="dock-label">Chat</span>
      </Link>
    </div>
  );
}
