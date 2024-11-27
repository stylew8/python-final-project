import React, { useState } from "react";
import '../styles/semesters.css';

export default function Semesters() {

    return (
        <main>
            <div className="container">
                <section className="semester">
                    <a href="/semestersDetails">
                         <h1>1 Semestras</h1>
                         <p>trukmė</p>
                    </a>
                    <a href="/semestersDetails">
                         <h1>2 Semestras</h1>
                         <p>trukmė</p>
                    </a>
                    <a href="/semestersDetails">
                         <h1>3 Semestras</h1>
                         <p>trukmė</p>
                    </a>
                    <a href="/semestersDetails">
                         <h1>4 Semestras</h1>
                         <p>trukmė</p>
                    </a>
                    <a href="/semestersDetails">
                         <h1>5 Semestras</h1>
                         <p>trukmė</p>
                    </a>
                    <a href="/semestersDetails">
                         <h1>6 Semestras</h1>
                         <p>trukmė</p>
                    </a>
                </section>
            </div>
        </main>
    );
}