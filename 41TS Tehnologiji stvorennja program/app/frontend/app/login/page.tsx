export default function Login() {
  return (
    <div className="min-h-screen flex items-center justify-center">
      {/* Card */}
      <div className="rounded-lg p-4 shadow-xs shadow-sky-100 flex-col flex gap-4">
        {/* Input Group */}
        <div className="flex-col gap-2">
          <label htmlFor="login">
            <span className="text-sm font-medium text-gray-700"> Login </span>
          </label>
          <input
            type="email"
            id="login"
            className="mt-0.5 w-full rounded border-gray-300 shadow-sm sm:text-sm p-2"
          ></input>
        </div>
        {/* Input Group */}
        <div className="flex-col gap-2">
          <label htmlFor="password">
            <span className="text-sm font-medium text-gray-700">Password</span>
          </label>
          <input
            type="password"
            id="password"
            className="mt-0.5 w-full rounded border-gray-300 shadow-sm sm:text-sm p-2"
          ></input>
        </div>
        {/* Signup Link */}
        <a
          href="/signup"
          className="text-sky-600 hover:underline decoration-sky-600 underline-offset-4"
        >
          Not registered yet?
        </a>
        {/* Button */}
        <button className="inline-block rounded-sm border border-sky-600 bg-sky-600 px-12 py-3 text-sm font-medium text-white hover:bg-transparent hover:text-sky-600 cursor-pointer">
          Login
        </button>
      </div>
    </div>
  );
}
