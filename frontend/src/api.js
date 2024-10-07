import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

export const fetchCreations = () => axios.get(`${API_URL}creations/`);
export const fetchCreation = (id) => axios.get(`${API_URL}creations/${id}/`);
export const createCreation = (data) => axios.post(`${API_URL}creations/`, data);
export const addComment = (creationId, data) => axios.post(`${API_URL}creations/${creationId}/add_comment/`, data);