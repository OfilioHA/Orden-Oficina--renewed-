import Cookie from 'js-cookie';
import { useEffect } from 'react';
import { useLocation, useNavigate } from "react-router";
import { useFetch } from '@/hooks/useFetch';

export function AliveProvider({ children }) {
    const navigate = useNavigate()
    const location = useLocation();
    const fetcher = useFetch();

    useEffect(() => {
        const token = Cookie.get('token');
        try {
            if (!token) throw new Error('Token no existe');
            fetcher.makeRequest('/auth/alive');
        } catch (error) {
            navigate('/login')
        }
    }, [location.pathname]);

    return children
}