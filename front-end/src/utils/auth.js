import { apiAuth } from "../api";

export const checkAuth = async () => {
    // Получаем токен из localStorage
    const token = localStorage.getItem("jwt");

    if(!token)
        return false;


    try {
        var response = await apiAuth("/verify-token");
      
        if(response.ok){
            return true;
        }
        else{
            localStorage.removeItem("jwt");
            return false;
        }
        
    } catch (error) {
        console.error("Authentication error:", error);
    }
  };
  