import Card from "@/components/Card";

export default function Home() {
  return (
    <div className="max-w-3xl mx-auto">
      <div className="flex flex-row gap-3 p-3">
        <input className="input flex-1" placeholder="Reference"></input>
        <input className="input flex-1" placeholder="Verse Text"></input>
        <button className="btn">Add</button>
      </div>
      <div className="flex flex-row flex-wrap gap-3 p-3">
        <Card
          text="For 'Whoever shall call on the name of the Lord will be saved.'"
          reference="Romans 10:13"
        />
        <Card
          text="For 'Whoever shall call on the name of the Lord will be saved.'"
          reference="Romans 10:13"
        />
        <Card
          text="For 'Whoever shall call on the name of the Lord will be saved.'"
          reference="Romans 10:13"
        />
      </div>
    </div>
  );
}
