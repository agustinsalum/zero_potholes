import { Link } from "react-router-dom";

export default function Navbar({ links, variant = "light" }) {
  return (
    <nav className={`navbar navbar-expand-lg bg-${variant}`}>
      <div className="container">
        <div className="navbar-nav mx-auto">
          {links.map((link) => (
            <Link key={link.to} className="nav-link mx-2 text-light" to={link.to}>
              {link.label}
            </Link>
          ))}
        </div>
      </div>
    </nav>
  );
}
