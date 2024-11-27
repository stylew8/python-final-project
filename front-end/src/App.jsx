import React, { useEffect, useState } from "react";

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { checkAuth } from "./utils/auth";
import Main from './pages/Main.jsx'
import Footer from './pages/Footer.jsx';
import Header from './pages/Header.jsx';

import LoginForm from './pages/LoginFrom.jsx';
import Semesters from './pages/Semesters.jsx';
import SemestersDetails from './pages/SemestersDetails.jsx';

import NotFound404 from './pages/NotFound404.jsx'
import 'bootstrap/dist/css/bootstrap.css';
import '@popperjs/core/dist/cjs/popper.js';
import '../src/styles/site.css'

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(null);

  useEffect(() => {
    const verifyAuth = async () => {
      const authStatus = await checkAuth();
      setIsAuthenticated(authStatus);
    };

    verifyAuth();
  }, []);

  if (isAuthenticated === null) {
    return (
      <main>
        <div>Loading...</div>
      </main>
    );
  }

  return (
    <BrowserRouter>
      <Header />
      <Routes>

        <Route path='/login' element={<LoginForm />} />
        <Route path='/semestersDetails' element={<SemestersDetails />} />
        <Route path='/semesters' element={<Semesters />} />
        <Route path='/' element={<Main />} />

        <Route
          path="/"
          element={isAuthenticated ? <Semesters /> : <Main />}
        />
        <Route path='*' element={<NotFound404 />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
