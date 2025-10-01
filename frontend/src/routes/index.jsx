import { Routes, Route, Navigate } from "react-router-dom";

import PublicLayout from "../layouts/PublicLayout";
import PrivateLayout from "../layouts/PrivateLayout";
import PrivateRoute from "../components/routing/PrivateRoute";

import Welcome from "../pages/public/Welcome";
import AboutPublic from "../pages/public/About";
import Reports from "../pages/private/Reports";
import AboutPrivate from "../pages/private/About";
import Login from "../pages/auth/Login";

export default function AppRoutes() {
  return (
    <Routes>
      {/* Rutas públicas */}
      <Route element={<PublicLayout />}>
        <Route path="/welcome" element={<Welcome />} />
        <Route path="/about" element={<AboutPublic />} />
        <Route path="/login" element={<Login />} />
      </Route>

      {/* Rutas privadas */}
      <Route
        element={
          <PrivateRoute>
            <PrivateLayout />
          </PrivateRoute>
        }
      >
        <Route path="/reports" element={<Reports />} />
        <Route path="/about-private" element={<AboutPrivate />} />
      </Route>

      {/* Redirección por defecto */}
      <Route path="*" element={<Navigate to="/welcome" />} />
    </Routes>
  );
}
