import React from "react";
import daisyui from "daisyui";

export default function App() {
  return (
    <div className="bg-white rounded-lg shadow-md p-8 max-w-lg mx-auto mt-8">
      <h1 className="text-3xl font-bold underline text-red-500 mb-4 text-center">
        Email
      </h1>
      <form className="flex flex-col">
        <textarea
          className="textarea mb-4"
          placeholder="Message"
          // Add additional classes from daisyUI for textarea styling
        ></textarea>
        <button
          type="submit"
          className="btn btn-primary w-full"
          // Add additional classes from daisyUI for button styling
        >
          Evaluate
        </button>
      </form>
    </div>
  );
}
