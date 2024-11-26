import logo from './logo.svg';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import './App.css';
import Main from './pages/Main.jsx'
import Footer from './pages/Footer.jsx';
import Header from './pages/Header.jsx';
import NotFound404 from './pages/NotFound404.jsx'

function App() {
  return (
      <BrowserRouter>
        <Header/>
          <Routes>
            <Route  path='/' element={<Main/>}/>
            <Route  path='*' element={<NotFound404/>}/>
          </Routes>
        <Footer/>
    </BrowserRouter>
  );
}

export default App;
