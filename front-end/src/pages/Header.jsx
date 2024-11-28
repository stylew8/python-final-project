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
        <ul className='nav'>
          <li className='nav-item' >
            <a className='nav-link' href="/semestersDetails">SemesterDetails</a>
          </li>
          <li className='nav-item' >
            <a className='nav-link' href="/semesters">Semesters</a>
          </li>
          <li className='nav-item' >
            <a className='nav-link' href="/studentView">StudentView</a>
          </li>
          <li className='nav-item' >
            <a className='nav-link' href="/studentSubjectDetailed">StudentSubjectView</a>
          </li>
        </ul>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
        </div>
      </div>
    </nav>
  )
}

export default Header