import React, { useState } from "react";
import '../styles/registerForm.css'

export default function RegistrationForm() {
    const [userType, setUserType] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
        // Handle registration logic here
        console.log("Registration submitted for user type:", userType);
    };

    return (
        <main>
            <form onSubmit={handleSubmit} className=" p-4 m-5 registration-form">
                <h2 className="text-center mb-4">Registracija</h2>

                <div className="mb-3">
                    <label htmlFor="userType" className="form-label">User Type</label>
                    <select
                        id="userType"
                        className="form-select"
                        value={userType}
                        onChange={(e) => setUserType(e.target.value)}
                        required
                    >
                        <option className="text-dark" value="student">Studentas</option>
                        <option className="text-dark" value="teacher">Mokytojas</option>
                    </select>
                </div>

                <div className="mb-3">
                    <label htmlFor="username" className="form-label">Vardas</label>
                    <input
                        type="text"
                        className="form-control"
                        id="username"
                        placeholder="Įveskite savo vardą"
                        required
                    />
                </div>

                <div className="mb-3">
                    <label htmlFor="email" className="form-label">El. paštas</label>
                    <input
                        type="email"
                        className="form-control"
                        id="email"
                        placeholder="Įveskite El. paštą"
                        required
                    />
                </div>

                <div className="mb-3">
                    <label htmlFor="password" className="form-label">Slaptažodis</label>
                    <input
                        type="password"
                        className="form-control"
                        id="password"
                        placeholder="Įveskite slaptažodį"
                        required
                    />
                </div>

                <div className="mb-3">
                    <label htmlFor="confirmPassword" className="form-label">Pakartotinai slaptažodis</label>
                    <input
                        type="password"
                        className="form-control"
                        id="confirmPassword"
                        placeholder="Įveskite slaptažodį pakartotinai"
                        required
                    />
                </div>

                <button type="submit" className="btn btn-secondary w-100">Registruotis</button>
            </form>
        </main>

    );
}
