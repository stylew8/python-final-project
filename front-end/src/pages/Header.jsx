import React from 'react'
import '../styles/header.css'

function Header() {
  return (
    <nav className="navbar navbar-expand-lg">
      <div className="container-fluid">
        <a className="navbar-brand" href="/">AIS</a>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon" />
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          {/* <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <a className="nav-link " href="#">Pamokos</a>
            </li>
            <li className="nav-item">
              <a className="nav-link " href="#">Tvarkaraštis</a>
            </li>
            <li className="nav-item">
              <a className="nav-link " href="#">Užduotys</a>
            </li>
            <li className="nav-item">
              <a className="nav-link " href="#">Įvertinimai</a>
            </li>
          </ul> */}
          {/* <form className="d-flex">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item" id='authorization'>
                <a className="nav-link" href="/login">Prisijungimas</a>
                <a className="nav-link" href="/register">Registracija</a>
              </li>
            </ul>
          </form> */}
        </div>
      </div>
    </nav>
  )
}

export default Header