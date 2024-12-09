import axios from 'axios';

const API = axios.create({
    baseURL: 'http://127.0.0.1:8000/', // Replace with your backend URL
});

export const sendCommand = (command) =>
    API.post('voice_assistant/', { command });