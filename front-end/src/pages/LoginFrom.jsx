import React, { useState } from "react";

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