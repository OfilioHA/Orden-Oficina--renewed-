import Cookie from 'js-cookie';
import { useNavigate } from 'react-router';
import { useUserStore } from '@/store/user';

export function useSession() {
    const navigate = useNavigate();
    const userStore = useUserStore((state) => state);

    const handleLogin = (token, user) => {
        Cookie.set('token', token, { expires: 1 });
        userStore.updateUser(user);
        navigate('/');
    }

    return {
        handleLogin,
        user: userStore.user
    }
}