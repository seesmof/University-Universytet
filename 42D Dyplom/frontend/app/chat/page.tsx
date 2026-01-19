import Link from "next/link";

export default function Chat() {
  return (
    <div className="dock">
      <Link href="owned/">
        <span className="dock-label">Owned</span>
      </Link>

      <Link href="/">
        <span className="dock-label">Store</span>
      </Link>

      <Link href="chat/" className="dock-active">
        <span className="dock-label">Chat</span>
      </Link>
    </div>
  );
}
