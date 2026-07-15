const baseUrl = "https://open-bible-api.vercel.app/";

export default function IndexPage() {
  return (
    <form className="p-3 flex flex-row gap-3 w-full">
      <input
        type="text"
        placeholder="Enter a Bible place in format `/Book_Abbreviation/Chapter_Number/Verse_Number/`"
        className="border p-3 rounded flex-1"
      />
      <button
        type="submit"
        className="bg-indigo-600 text-white rounded p-3 px-4 cursor-pointer hover:bg-indigo-700"
      >
        Search
      </button>
    </form>
  );
}
