export default function Home() {
  return (
    <div className="max-w-3xl mx-auto p-2">
      <div className="flex flex-row gap-2">
        <input className="input" placeholder="Reference"></input>
        <input className="input" placeholder="Verse Text"></input>
        <button className="btn">Add</button>
      </div>
    </div>
  );
}
