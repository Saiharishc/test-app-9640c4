import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [health, setHealth] = useState('Loading...');
  const [testData, setTestData] = useState('Loading...');

  useEffect(() => {
    fetch('/api/health')
      .then(response => response.json())
      .then(data => setHealth(data.status))
      .catch(error => console.error('Error fetching health:', error));

    fetch('/api/test')
      .then(response => response.json())
      .then(data => setTestData(data.message))
      .catch(error => console.error('Error fetching test data:', error));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to Test App</h1>
        <p>Health Check: {health}</p>
        <p>Test Endpoint: {testData}</p>
      </header>
    </div>
  );
}

export default App;
