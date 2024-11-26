import React from "react";
import '../styles/index.css'

import studentImg from '../images/student.png';
import teacherImg from '../images/teacher.png';
import adminImg from '../images/whiteboard.png';

export default function Main() {
    return (
        <main className="landing-page">
            <h1>Prašome prisijungti prie paskyros</h1>
            <section>
                <a className="student-log" href="#">
                    <img src={studentImg} alt="Logo" />
                    <h2>Studentas</h2>
                </a>
                <a className="teacher-log"  href="#">
                    <img src={teacherImg} alt="Logo" />
                    <h2>Mokytojas</h2>
                </a>
                <a className="admin-log"  href="#">
                    <img src={adminImg} alt="Logo" />
                    <h2>Administratorius</h2>
                </a>
            </section>
        </main>
    );
}