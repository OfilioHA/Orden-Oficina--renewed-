import axios from "axios";

export function createAxios(url, config) {
  return axios.create({
    baseURL: `${url}`,
    ...config,
  });
}

export function createServerAxios() {
  const url = import.meta.env.VITE_SERVER_URL;
  const axios = createAxios(url);
  return axios;
}
