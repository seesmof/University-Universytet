export default function Home() {
  return (
    <div className="dock">
      <button>
        <span className="dock-label">Home</span>
      </button>

      <button className="dock-active">
        <span className="dock-label">Inbox</span>
      </button>

      <button>
        <span className="dock-label">Settings</span>
      </button>
    </div>
  );
}
