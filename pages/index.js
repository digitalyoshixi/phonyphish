import { useState, useEffect } from "react";
export default function Home() {
    const [search, setSearch] = useState("");
    const calls = [
      { number: "000-000-0000", location: "Toronto, Canada", date: "2025-01-18", time: "10:30 AM", status: "Scam" },
      { number: "416-000-0000", location: "New York, United States", date: "2025-01-17", time: "03:00 PM", status: "Safe" },
    ];

    const filteredCalls = calls.filter((call) => call.number.includes(search));
  
    const handleReport = async (number) => {

        const response = await fetch('ec2-184-73-58-196.compute-1.amazonaws.com:8000/dbupdate', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ number: true }),
        });
        
        if (!response.ok) {
          throw new Error('Something went wrong!');
        }
        alert(`The call with number ${number} has been successfully reported.`);
      

    };
  
    return (
      <div className="p-4">
          <img style={{position: 'absolute', top: 0, left: 0}} width="60" className="m-4 rounded-lg" src="/cover1.png"></img>          
        <div className="flex flex-row justify-center">
          <h1 className="text-5xl font-extrabold text-center">Phoney Phishing</h1>
        </div>
        <div className="flex justify-center">
          <button className="p-3 m-5 rounded-md font-bold text-5xl text-white bg-red-500">Call</button>
        </div>
        <header className="bg-blue-800 text-white py-4 px-6 rounded mb-4">
          <h1 className="text-2xl font-bold">Recent Calls</h1>
          <p className="text-sm">Search for a Recent Call</p>
        </header>
        <div className="mb-4">
          <input
            type="text"
            placeholder="Search Phone Number"
            className="w-full px-4 py-2 border rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </div>
        <div>
          {filteredCalls.map((call, index) => (
            <div key={index} className="bg-white shadow-md rounded p-4 mb-4 border border-gray-200">
              <div className="flex justify-between">
                <div>
                  <p className="font-bold">{call.number}</p>
                  <p className="text-gray-500">Location: {call.location}</p>
                  <p className="text-gray-500">Date: {call.date}</p>
                  <p className="text-gray-500">Time: {call.time}</p>
                </div>
                <div className="flex items-center space-x-4">
                  <div
                    className={`flex items-center ${
                      call.status === "Scam" ? "text-red-500" : "text-green-500"
                    }`}
                  >
                    <span className="material-icons">
                      {call.status === "Scam" ? "warning" : "check_circle"}
                    </span>
                    <span>{call.status}</span>
                  </div>
                  <button
                    className={`${
                      call.status === "Scam" ? "bg-red-500 hover:bg-red-600" : "bg-blue-500 hover:bg-blue-600"
                    } text-white px-4 py-2 rounded shadow`}
                    onClick={() => handleReport(call.number)}
                  >
                    Report
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  }
  