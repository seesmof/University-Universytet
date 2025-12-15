"use client";

import { useState } from "react";

export default function Signup() {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const [passwordConfirmation, setPasswordConfirmation] = useState("");

  const handleRegister = () => {
    if (password !== passwordConfirmation) {
      alert("Passwords do not match");
      return;
    }

    sessionStorage.setItem("user", name);
    sessionStorage.setItem("password", password);
    window.location.href = "/main";
  };

  return (
    <div className="min-h-screen flex items-center justify-center">
      {/* Card */}
      <div className="rounded-lg p-4 shadow-xs shadow-sky-100 flex-col flex gap-4">
        {/* Login Input Group */}
        <div className="flex-col gap-2">
          <label htmlFor="login">
            <span className="text-sm font-medium text-gray-700"> Login </span>
          </label>
          <input
            type="text"
            id="login"
            className="mt-0.5 w-full rounded border-gray-300 shadow-sm sm:text-sm p-2"
            onChange={(e) => setName(e.target.value)}
            value={name}
          ></input>
        </div>
        {/* Password Input Group */}
        <div className="flex-col gap-2">
          <label htmlFor="passwordFirst">
            <span className="text-sm font-medium text-gray-700">Password</span>
          </label>
          <input
            type="password"
            id="passwordFirst"
            className="mt-0.5 w-full rounded border-gray-300 shadow-sm sm:text-sm p-2"
            onChange={(e) => setPassword(e.target.value)}
            value={password}
          ></input>
        </div>
        {/* Password Confirmation Input Group */}
        <div className="flex-col gap-2">
          <label htmlFor="passwordSecond">
            <span className="text-sm font-medium text-gray-700">
              Password Confirmation
            </span>
          </label>
          <input
            type="password"
            id="passwordSecond"
            className="mt-0.5 w-full rounded border-gray-300 shadow-sm sm:text-sm p-2"
            onChange={(e) => setPasswordConfirmation(e.target.value)}
            value={passwordConfirmation}
          ></input>
        </div>
        {/* Login Link */}
        <a
          href="/login"
          className="text-sky-600 hover:underline decoration-sky-600 underline-offset-4"
        >
          Already registered?
        </a>
        {/* Button */}
        <button
          className="inline-block rounded-sm border border-sky-600 bg-sky-600 px-12 py-3 text-sm font-medium text-white hover:bg-transparent hover:text-sky-600 cursor-pointer"
          onClick={handleRegister}
        >
          Sign Up
        </button>
      </div>
    </div>
  );
}
