import React, { useState } from "react";

const App = () => {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Remove punctuation from text
    const textWithoutPunctuation = text.replace(/[^\w\s]|_/g, "").replace(/\s+/g, " ");
    setText(textWithoutPunctuation);

    try {
      const response = await fetch(`http://127.0.0.1:8000/api/predict/${textWithoutPunctuation}/`);
      if (response.ok) {
        const data = await response.json();
        setResult(data);
        setError(null);
      } else {
        setError(`Error in fetching score of text: ${textWithoutPunctuation}`);
        setResult(null);
      }
    } catch (error) {
      setError(`Error in fetching score of text: ${textWithoutPunctuation}`);
      setResult(null);
    }
  };

  return (
    <div className="bg-gray-200 min-h-screen flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-md">
        <h1 className="text-2xl font-bold mb-4">Text Prediction App</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            className="w-full border-gray-300 border p-2 rounded-md mb-4"
            placeholder="Enter text"
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 px-4 rounded-md"
          >
            Predict
          </button>
        </form>
        {result && (
          <div className="mt-4">
            <h2 className="text-xl font-semibold">Prediction:</h2>
            <p className="mt-2">{result}</p>
          </div>
        )}
        {error && <p className="text-red-500 mt-4">{error}</p>}
      </div>
    </div>
  );
};

export default App;
