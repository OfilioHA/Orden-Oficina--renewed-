import { Navigate, Route, Routes } from "react-router";
// Layouts
import { DefaultLayout } from "./layouts/default";
import { CleanLayout } from "./layouts/clean";
// Pages
import { LoginPage } from "./pages/login";
import { HomePage } from "./pages/home";
import { Page404 } from "./pages/404";

export function AppRouter() {
    return (
        <Routes>
            <Route path="/" element={<DefaultLayout />}>
                <Route index element={<HomePage />} />
            </Route>
            <Route path="/" element={<CleanLayout />}>
                <Route path="login" element={<LoginPage />} />
            </Route>
            <Route path="/404" element={<Page404 />} />
            <Route path="*" element={<Navigate to={'/404'} />} />
        </Routes>
    )
}