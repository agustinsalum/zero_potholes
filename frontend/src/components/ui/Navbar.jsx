const textClass = variant === "dark" ? "text-light" : "text-dark";

<Link key={link.to} className={`nav-link mx-2 ${textClass}`} to={link.to}>
