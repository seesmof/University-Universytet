import Image from "next/image";

export default function Home() {
  return (
    <div className="min-h-screen bg-sky-50 flex gap-3 flex-col items-center justify-center">
      {/* Table */}
      {/* <div className="rounded-md p-4 bg-red-500"></div> */}
      {/* Main App */}
      <div className="rounded-md bg-white border-2 border-sky-300 flex flex-col p-3 gap-4">
        <div className="flex flex-col gap-1">
          <label htmlFor="givenText">Given text</label>
          <input
            type="text"
            id="givenText"
            className="outline-2 rounded-md outline-sky-300 focus:outline-sky-500 px-2"
            placeholder="For example, Some text..."
          />
        </div>

        <div className="flex flex-col gap-1">
          <label htmlFor="keyInput">Key</label>
          <input
            type="text"
            id="keyInput"
            className="outline-2 rounded-md outline-sky-300 focus:outline-sky-500 px-2"
            placeholder="For example, GOD"
          />
        </div>

        <div className="flex flex-row gap-3">
          <button className="bg-sky-50 p-1 hover:bg-sky-200 w-full rounded-md">
            Encrypt
          </button>
          <button className="bg-sky-50 p-1 hover:bg-sky-200 w-full rounded-md">
            Decrypt
          </button>
        </div>
      </div>
      {/* History */}
      {/* <div className="rounded-md p-4 bg-red-500"></div> */}
    </div>
  );
}
