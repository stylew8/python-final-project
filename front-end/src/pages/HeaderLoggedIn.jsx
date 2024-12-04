import React from 'react'
import '../styles/header.css'



function Header() {
  const handleLogout = () => {
    // Remove JWT token from localStorage
    localStorage.removeItem('jwt'); // or use the exact key where the JWT is stored
    
    // Optionally, you can redirect the user after logging out
    window.location.href = '/'; // or use React Router to redirect if needed
  };

  return (
    <nav className="navbar navbar-expand-lg">
      <div className="container-fluid">
        <a className="navbar-brand" href="/">AIS</a>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon" />
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <a className="nav-link " onClick={handleLogout} href="#">Atsijungti</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Header