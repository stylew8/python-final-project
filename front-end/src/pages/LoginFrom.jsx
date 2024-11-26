import React, { useState } from "react";
import '../styles/loginForm.css'

export default function LoginForm() {
    const [userType, setUserType] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
        // Handle login logic here
        console.log("Login submitted for user type:", userType);
    };

    return (
        <main>
            <form onSubmit={handleSubmit} className="p-4 m-5 login-form">
                <h2 className="text-center mb-4">Prisijungimas</h2>

                <div className="mb-3">
                    <label htmlFor="userType" className="form-label">Asmens tipas</label>
                    <select
                        id="userType"
                        className="form-select text-dark"
                        value={userType}
                        onChange={(e) => setUserType(e.target.value)}
                        required
                    >
                        <option className="text-dark" value="student">Studentas</option>
                        <option className="text-dark" value="teacher">Mokytojas</option>
                        <option className="text-dark" value="admin">Administratorius</option>
                    </select>
                </div>

                <div className="mb-3">
                    <label htmlFor="username" className="form-label">Vardas</label>
                    <input
                        type="text"
                        className="form-control"
                        id="username"
                        placeholder="Įveskite vardą"
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

                <button type="submit" className="btn btn-secondary w-100">Prisijungti</button>
            </form>
        </main>

    );
}