import axios from 'axios';
const api = axios.create({
    baseURL: 'http://cmacedog.pythonanywhere.com',
});

export default api;