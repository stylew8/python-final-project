import React, { useState } from "react";

const LoginForm = ({ userType }) => {
    

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError(""); 
        setLoading(true); 

        try {
            var role = userType;

            const response = await fetch("http://localhost:8000/login/" + userType, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ username, password, role }),
            });

            const data = await response.json();

            if (response.ok) {
                const { token } = data;
                localStorage.setItem("jwt", token); 
                console.log("Login successful:", token);
                // Например, window.location.href = "/dashboard";
            } else {
                setError("Neteisingas vardas arba slaptažodis");
            }
        } catch (err) {
            console.error("Login error:", err);
            setError("Klaida prisijungiant prie serverio");
        } finally {
            setLoading(false); 
        }
    };


    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

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
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
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
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>

                {error && <div className="alert alert-danger">{error}</div>}

                <button type="submit" className="btn btn-secondary w-100" disabled={loading}>
                    {loading ? "Prašome palaukti..." : "Prisijungti"}
                </button>
            </form>
        </main>
    );
}

export default LoginForm;