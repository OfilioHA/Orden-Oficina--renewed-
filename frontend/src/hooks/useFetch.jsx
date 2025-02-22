import { useEffect, useState } from "react";

export function useFetch(url, options) {
    const appMode = import.meta.env.VITE_APP_MODE;

    const [data, setData] = useState(null);
    const [status, setStatus] = useState(null);
    const [loading, setLoading] = useState(false);
    const [response, setResponse] = useState({});

    const makeRequest = async (url, options) => {
        setLoading(true);
        let localResponse = null;

        try {
            localResponse = await axios.request({url, ...options});
        } catch (error) {
            localResponse = error.response;
        } finally {
            if (localResponse == undefined) localResponse = null;
            setResponse(localResponse);
            setData(localResponse?.data ?? []);
            setStatus(localResponse?.status);
            setLoading(false);
        }

        return localResponse;
    };

    const cleanRequest = async () => {
        setData(null);
        setStatus(null);
        setLoading(false);
        setResponse({});
    };

    useEffect(() => {
        if (!url) return;
        (async function () {
            await makeRequest(url, options);
        })();
    }, [url, options?.params]);

    useEffect(() => {
        if (!response || !Object.keys(response).length) return;
        if (!response.data?.message) return;
        const development = appMode == "development";
        console.log(response.data?.message);
    }, [response]);

    return {
        data,
        status,
        loading,
        response,
        makeRequest,
        cleanRequest
    };
}
