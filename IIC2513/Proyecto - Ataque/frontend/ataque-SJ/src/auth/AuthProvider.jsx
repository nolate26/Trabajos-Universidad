import { useEffect, useState } from "react";
import { AuthContext } from "./AuthContext";

function AuthProvider({ children }) {
    const [token, setToken] = useState(localStorage.getItem('token') || null);
    const [id, setId] = useState(localStorage.getItem('id') || null);
    const [gameId, setGameId] = useState(localStorage.getItem('gameId') || null);

    function logout() {
        setToken(null)
        setId(null)
    }


    useEffect(() => {
        localStorage.setItem('token', token);
    }, [token]);

    useEffect(() => {
        localStorage.setItem('id', id);
    }, [id]);

    useEffect(() => {
        localStorage.setItem('gameId', gameId);
    }, [gameId]);


    return (
        <AuthContext.Provider value={{ token, setToken, logout, id, setId, gameId, setGameId }}>
            {children}
        </AuthContext.Provider>
    );
}
export default AuthProvider;
