"use client";

import { useState } from "react";

export default function IndexPage() {
  const [selectedChat, setSelectedChat] = useState<number>(0);

  return (
    <div className="min-h-screen bg-sky-50 flex gap-3 p-3">
      <div className="bg-white w-60 rounded-lg flex flex-col overflow-hidden">
        {/* Messages */}
        <div
          id="chat0"
          className={`w-full p-3 hover:bg-sky-100 cursor-pointer ${selectedChat === 0 ? "bg-sky-100" : ""}`}
          onClick={() => setSelectedChat(0)}
        >
          <h2 className="font-bold">Oleh</h2>
          <p className="text-sm">Last message is this...</p>
        </div>
        <div
          id="chat1"
          className={`w-full p-3 hover:bg-sky-100 cursor-pointer ${selectedChat === 1 ? "bg-sky-100" : ""}`}
          onClick={() => setSelectedChat(1)}
        >
          <h2 className="font-bold">Seesm</h2>
          <p className="text-sm">Last message is different...</p>
        </div>
        <div
          id="chat2"
          className={`w-full p-3 hover:bg-sky-100 cursor-pointer ${selectedChat === 2 ? "bg-sky-100" : ""}`}
          onClick={() => setSelectedChat(2)}
        >
          <h2 className="font-bold">Marvin</h2>
          <p className="text-sm">Texting brother Marvin here...</p>
        </div>
      </div>
      <div className="bg-white flex-1 w-60 rounded-lg"></div>
    </div>
  );
}
