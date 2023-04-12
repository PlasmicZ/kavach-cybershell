import React from "react";
import "daisyui/dist/daisyui.css";

export default function App() {
  return (
    <div className="bg-white rounded-lg shadow-md p-8 max-w-lg mx-auto mt-8">
      <h1 className="text-3xl font-bold underline text-red-500 mb-4">
        Compose Email
      </h1>
      <form className="flex flex-col">
        <input
          type="text"
          className="input mb-4"
          placeholder="To"
          // Add additional classes from daisyUI for input styling
        />
        <input
          type="text"
          className="input mb-4"
          placeholder="Subject"
          // Add additional classes from daisyUI for input styling
        />
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
          Send
        </button>
      </form>
    </div>
  );
}
