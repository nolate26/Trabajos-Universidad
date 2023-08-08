import { BrowserRouter, Routes, Route } from "react-router-dom"

import UserWelcome from '../profile/UserWelcome'
import App from "./App"
import Instructions from "../game/Instructions"
import PaginaPrincipal from "./PaginaPrincipal"
import Partidas from "./Partidas"
import Login from "../profile/Login"
import Signup from '../profile/Signup'
import Game from "../game/Game"
import AdminCheck from '../protected/AdminCheck'
import UserCheck from '../protected/UserCheck'
import LogoutButton from '../profile/Logout'
import CreateGame from '../game/CreateGame'

function Routing() {
    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route path={'/instructions'} element={<Instructions />} />
                    <Route path={'/sobre-nosotros'} element={<UserWelcome />} />
                    <Route path={'/pagina-principal'} element={<PaginaPrincipal />} />
                    <Route path={'/login'} element={<Login />} />
                    <Route path={"/signup"} element={<Signup />} />
                    <Route path={'/partidas'} element={<Partidas />} />
                    <Route path={'/game'} element={<Game />} />
                    <Route path={'/create-game'} element={<CreateGame />} />
                    <Route path={'/'} element={<App />} />
                    <Route path={"/admincheck"} element={<AdminCheck />} />
                    <Route path={"/usercheck"} element={<UserCheck />} />
                </Routes>
            </BrowserRouter>
        </>
    )
}

export default Routing
