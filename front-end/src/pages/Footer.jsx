import React from 'react'
import '../styles/footer.css'

function Footer() {
  return (
    <div class="def-footer">
      <footer class="d-flex flex-wrap justify-content-between align-items-center border-top">
        <p class=" nav-link">© 2024 TAMO KLONAS, Inc</p>

        <ul class="nav justify-content-end">
          <li class="nav-item"><a href="#" class="nav-link px-2 ">Tvarkaraštis</a></li>
          <li class="nav-item"><a href="#" class="nav-link px-2 ">DUK</a></li>
          <li class="nav-item"><a href="#" class="nav-link px-2 ">Privatumo politika</a></li>
        </ul>
      </footer>
    </div>
  )
}

export default Footer