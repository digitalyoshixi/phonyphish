// pages/index.js

export default function Home() {
    return (
      <div className="p-4">
        {/* Header Section */}
        <header className="bg-blue-800 text-white py-4 px-6 rounded mb-4">
          <h1 className="text-2xl font-bold">Recent Calls</h1>
          <p className="text-sm">Search for a Recent Call</p>
        </header>
  
        {/* Search Bar */}
        <div className="mb-4">
          <input
            type="text"
            placeholder="Search Phone Number"
            className="w-full px-4 py-2 border rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
  
        {/* Recent Calls List */}
        <div>
          {/* Call 1 */}
          <div className="bg-white shadow-md rounded p-4 mb-4 border border-gray-200">
            <div className="flex justify-between">
              {/* Call Details */}
              <div>
                <p className="font-bold">000-000-0000</p>
                <p className="text-gray-500">Location: Toronto, Canada</p>
                <p className="text-gray-500">Date: 2025-01-18</p>
                <p className="text-gray-500">Time: 10:30 AM</p>
              </div>
  
              {/* Call Actions */}
              <div className="flex items-center space-x-4">
                <div className="text-red-500 flex items-center">
                  <span className="material-icons">warning</span>
                  <span>Scam</span>
                </div>
                <button className="bg-red-500 text-white px-4 py-2 rounded shadow hover:bg-red-600">
                  Report
                </button>
              </div>
            </div>
          </div>
  
          {/* Call 2 */}
          <div className="bg-white shadow-md rounded p-4 mb-4 border border-gray-200">
            <div className="flex justify-between">
              {/* Call Details */}
              <div>
                <p className="font-bold">416-000-0000</p>
                <p className="text-gray-500">Location: New York, United States</p>
                <p className="text-gray-500">Date: 2025-01-17</p>
                <p className="text-gray-500">Time: 03:00 PM</p>
              </div>
  
              {/* Call Actions */}
              <div className="flex items-center space-x-4">
                <div className="text-green-500 flex items-center">
                  <span className="material-icons">check_circle</span>
                  <span>Safe</span>
                </div>
                <button className="bg-blue-500 text-white px-4 py-2 rounded shadow hover:bg-blue-600">
                  Report
                </button>
              </div>
            </div>
          </div>
        </div>

      </div>
    );
  }