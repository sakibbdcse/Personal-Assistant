import React, { useState } from 'react';
import { sendCommand } from '../services/api';

const VoiceAssistant = () => {
  const [command, setCommand] = useState('');
  const [response, setResponse] = useState('');

  const handleSend = async () => {
    try {
      const result = await sendCommand(command);
      setResponse(result.data.response);
    } catch (error) {
      console.error(error);
      setResponse('Error communicating with the server.');
    }
  };

  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      <h1>Voice Assistant</h1>
      <input
        type="text"
        value={command}
        onChange={(e) => setCommand(e.target.value)}
        placeholder="Enter your command"
        style={{ padding: '10px', width: '300px' }}
      />
      <button onClick={handleSend} style={{ marginLeft: '10px', padding: '10px' }}>
        Send
      </button>
      {response && <p>Response: {response}</p>}
    </div>
  );
};

export default VoiceAssistant;
