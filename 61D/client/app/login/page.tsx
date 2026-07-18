import Link from "next/link";

export default function LoginPage() {
  return (
    <div className="rounded-md border p-3 mx-auto max-w-md w-full my-auto">
      <form className="flex flex-col gap-3">
        <div className="flex flex-col gap-1">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            className="border p-1 rounded-md"
            placeholder="Your email address..."
          />
        </div>

        <div className="flex flex-col gap-1">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            className="border p-1 rounded-md"
            placeholder="Your password..."
          />
        </div>

        <div className="flex gap-1">
          <button
            type="button"
            className="text-white bg-slate-600 hover:bg-slate-500 cursor-pointer rounded-md p-1 px-4"
          >
            <Link href={"/signup/"}>Sign Up</Link>
          </button>
          <button
            type="submit"
            className="bg-sky-600 text-white rounded-md hover:bg-sky-500 cursor-pointer p-1 flex-1"
          >
            Log in
          </button>
        </div>
      </form>
    </div>
  );
}
