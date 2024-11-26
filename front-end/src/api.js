export const apiNoAuth = async (endpoint, method = "GET", data = null) => {
    const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || "http://localhost:8000";

    const headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    };

    let body = null;
    if (data) {
        body = new URLSearchParams();
        for (const key in data) {
            body.append(key, data[key]);
        }
    }

    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            method,
            headers,
            body,
        });

        return await response;
    } catch (error) {
        console.error("Fetch Error:", error);
        throw error;
    }
};


export const apiAuth = async (endpoint, method = "GET", data = null) => {
    const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || "http://localhost:8000";

    const headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    };

    const token = localStorage.getItem("jwt");

    if (token) {
        headers["Authorization"] = `Bearer ${token}`;
    }

    let body = null;
    if (data) {
        body = new URLSearchParams();
        for (const key in data) {
            body.append(key, data[key]);
        }
    }

    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            method,
            headers,
            body,
        });

        return response;
    } catch (error) {
        console.error("Fetch Error:", error);
        throw error;
    }
};