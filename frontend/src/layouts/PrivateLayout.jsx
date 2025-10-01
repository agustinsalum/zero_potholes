import { Outlet } from "react-router-dom";
import Navbar from "../components/ui/Navbar";

export default function PrivateLayout() {
  const links = [
    { to: "/reports", label: "Reports" },
    { to: "/about-private", label: "About" },
  ];

  return (
    <>
      <Navbar links={links} variant="dark" />
      <main className="container mt-4">
        <Outlet />
      </main>
    </>
  );
}
