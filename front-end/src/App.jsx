import logo from './logo.svg';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import Main from './pages/Main.jsx'
import Footer from './pages/Footer.jsx';
import Header from './pages/Header.jsx';

import LoginForm from './pages/LoginFrom.jsx';
import Semesters from './pages/Semesters.jsx';

import NotFound404 from './pages/NotFound404.jsx'
import 'bootstrap/dist/css/bootstrap.css';
import '@popperjs/core/dist/cjs/popper.js';
import '../src/styles/site.css'

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path='/login' element={<LoginForm />} />
        <Route path='/semesters' element={<Semesters />} />
        <Route path='/' element={<Main />} />
        <Route path='*' element={<NotFound404 />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
