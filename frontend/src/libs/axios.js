import axios from "axios";
import Cookie from 'js-cookie';

export function createAxios(url, config) {
  return axios.create({
    baseURL: `${url}`,
    ...config,
  });
}

export function createServerAxios() {
  const url = import.meta.env.VITE_SERVER_URL;
  const axios = createAxios(url);

  axios.interceptors.request.use((config) => {
      const token = Cookie.get('token');
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    }, (error) => Promise.reject(error)
  );

  return axios;
}
