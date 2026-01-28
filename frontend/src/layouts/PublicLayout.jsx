import { Outlet } from "react-router-dom";
import Navbar from "../components/ui/Navbar";

export default function PublicLayout() {
  const links = [
    { to: "/", label: "Welcome" },
    { to: "/about", label: "About" },
  ];

  return (
    <>
      <Navbar links={links} variant="transparent" />
      <main className="container mt-4">
        <Outlet />
      </main>
    </>
  );
}
