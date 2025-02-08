import { Route, Routes } from "react-router";
import { DefaultLayout } from "./layouts/default";
import { CleanLayout } from "./layouts/clean";
import { LoginPage } from "./pages/login";
import { HomePage } from "./pages/home";


export function AppRouter() {
    return (
        <Routes>
            <Route path="/" element={<DefaultLayout />}>
                <Route index element={<HomePage />} />
            </Route>
            <Route path="/" element={<CleanLayout />}>
                <Route path="login" element={<LoginPage />} />
            </Route>
        </Routes>
    )
}