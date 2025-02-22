import { useNavigate } from 'react-router';

export function useSession() {
    const navigate = useNavigate();

    const handleLogin = (token, user) => {
        window.axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        navigate('/');
    }

    return {
        handleLogin
    }
}