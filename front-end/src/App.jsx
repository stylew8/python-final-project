import React, { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { checkAuth } from "./utils/auth";

import Main from './pages/Main.jsx'
import Footer from './pages/Footer.jsx';
import Header from './pages/Header.jsx';
import HeaderLoggedIn from './pages/HeaderLoggedIn.jsx';
import LoginForm from './pages/LoginFrom.jsx';
import Semesters from './pages/Semesters.jsx';
import SemestersDetails from './pages/SemestersDetails.jsx';
import StudentView from './pages/StudentView.jsx';
import StudentSubjectDetailed from './pages/StudentSubjectDetailed.jsx';
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
      {isAuthenticated ? <HeaderLoggedIn /> : <Header />}
      <Routes>
        <Route
          path="/"
          element={isAuthenticated ? <Semesters /> : <Main />}
        />
        <Route path='/semestersDetails' element={<SemestersDetails />} />
        <Route path='/studentView/:semesterId' element={<StudentView />} />
        <Route path="/studentSubjectDetailed/:subjectId" element={<StudentSubjectDetailed />} />
        <Route path='*' element={<NotFound404 />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
