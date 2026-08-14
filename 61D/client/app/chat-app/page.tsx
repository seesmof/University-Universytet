"use client";

import { useState } from "react";

export default function IndexPage() {
  const [selectedChat, setSelectedChat] = useState<number>(0);

  return (
    <div className="min-h-screen overflow-hidden flex">
      {/* Chats Window */}
      <aside className="w-64 flex flex-col border-r-2 h-screen fixed">
        {/* Chats go here */}
        <div
          id="chat-0"
          className={`w-full p-3 hover:bg-sky-100 cursor-pointer ${selectedChat === 0 ? "bg-sky-100" : ""}`}
          onClick={() => setSelectedChat(0)}
        >
          <h2 className="font-bold">Oleh</h2>
          <p className="text-sm">Last message is this...</p>
        </div>
        <div
          id="chat-1"
          className={`w-full p-3 hover:bg-sky-100 cursor-pointer ${selectedChat === 1 ? "bg-sky-100" : ""}`}
          onClick={() => setSelectedChat(1)}
        >
          <h2 className="font-bold">Seesm</h2>
          <p className="text-sm">Last message is different...</p>
        </div>
        <div
          id="chat-2"
          className={`w-full p-3 hover:bg-sky-100 cursor-pointer ${selectedChat === 2 ? "bg-sky-100" : ""}`}
          onClick={() => setSelectedChat(2)}
        >
          <h2 className="font-bold">Marvin</h2>
          <p className="text-sm">Texting brother Marvin here...</p>
        </div>
      </aside>

      {/* Messages Window */}
      <main className="flex-1 overflow-y-auto ml-64 flex flex-col">
        <div className="bg-white w-full fixed">
          <h3 className="font-bold p-3">
            {selectedChat === 0
              ? "Oleh"
              : selectedChat === 1
                ? "Seesm"
                : "Marvin"}
          </h3>
        </div>

        {/* Messages Container */}
        <div className="flex flex-col gap-3 p-3 pt-12">
          <div className="bg-sky-600 p-3 w-fit text-white rounded-r-lg rounded-t-lg">
            <p>Hey there!</p>
            <span className="text-sm mt-1 text-sky-100">Read</span>
          </div>
          <div className="bg-sky-600 p-3 w-fit text-white rounded-l-lg rounded-t-lg self-end">
            <p>Hello, praise King Jesus!</p>
            <span className="text-sm mt-1 text-sky-100">Sent</span>
          </div>
          <div className="bg-sky-600 p-3 w-fit text-white rounded-r-lg rounded-t-lg">
            <p>Hey there!</p>
            <span className="text-sm mt-1 text-sky-100">Read</span>
          </div>
          <div className="bg-sky-600 p-3 w-fit text-white rounded-l-lg rounded-t-lg self-end">
            <p>Hello, praise King Jesus!</p>
            <span className="text-sm mt-1 text-sky-100">Sent</span>
          </div>
          <div className="bg-sky-600 p-3 w-fit text-white rounded-r-lg rounded-t-lg">
            <p>Hey there!</p>
            <span className="text-sm mt-1 text-sky-100">Read</span>
          </div>
          <div className="bg-sky-600 p-3 w-fit text-white rounded-l-lg rounded-t-lg self-end">
            <p>Hello, praise King Jesus!</p>
            <span className="text-sm mt-1 text-sky-100">Sent</span>
          </div>
          <div className="bg-sky-600 p-3 w-fit text-white rounded-r-lg rounded-t-lg">
            <p>Hey there!</p>
            <span className="text-sm mt-1 text-sky-100">Read</span>
          </div>
          <div className="bg-sky-600 p-3 w-fit text-white rounded-l-lg rounded-t-lg self-end">
            <p>Hello, praise King Jesus!</p>
            <span className="text-sm mt-1 text-sky-100">Sent</span>
          </div>
          <div className="bg-sky-600 p-3 w-fit text-white rounded-r-lg rounded-t-lg">
            <p>Hey there!</p>
            <span className="text-sm mt-1 text-sky-100">Read</span>
          </div>
          <div className="bg-sky-600 p-3 w-fit text-white rounded-l-lg rounded-t-lg self-end">
            <p>Hello, praise King Jesus!</p>
            <span className="text-sm mt-1 text-sky-100">Sent</span>
          </div>
          <div className="bg-sky-600 p-3 w-fit text-white rounded-r-lg rounded-t-lg">
            <p>Hey there!</p>
            <span className="text-sm mt-1 text-sky-100">Read</span>
          </div>
          <div className="bg-sky-600 p-3 w-fit text-white rounded-l-lg rounded-t-lg self-end">
            <p>Hello, praise King Jesus!</p>
            <span className="text-sm mt-1 text-sky-100">Sent</span>
          </div>
        </div>

        <div className="flex gap-3 p-3 bg-white">
          <input
            type="text"
            className="outline w-full rounded-lg outline-sky-600 px-4 py-2"
            placeholder="Your message here..."
          />
          <button className="bg-sky-600 cursor-pointer hover:bg-sky-700 text-white px-4 rounded-lg">
            Send
          </button>
        </div>
      </main>
    </div>
  );
}
