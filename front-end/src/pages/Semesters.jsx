import React, { useEffect, useState } from "react";
import '../styles/semesters.css';
import { apiAuth } from "../api";

export default function Semesters() {
     const [semesters, setSemesters] = useState([]);
     const [loading, setLoading] = useState(true);
     const [error, setError] = useState(null);

     useEffect(() => {
          const fetchSemesters = async () => {
               try {
                    const response = await apiAuth("/students/semesters");
                    const data = await response.json();
                    setSemesters(data);
               } catch (error) {
                    setError("Failed to load semesters");
               } finally {
                    setLoading(false);
               }
          };

          fetchSemesters();
     }, []);

     if (loading) {
          return <div>Loading...</div>; 
     }

     if (error) {
          return <div>{error}</div>; 
     }

     return (
          <main>
               <div className="container">
                    <section className="semester">
                    {semesters.length === 0 ? (
                              <div>No available semesters</div>
                         ) : (
                              semesters.map((semester, index) => (
                                   <a key={index} href="/semestersDetails">
                                        <h1>{semester.name}</h1>
                                        <p>{semester.start_date} - {semester.end_date}</p> 
                                   </a>
                              ))
                         )}
                    </section>
               </div>
          </main>
     );
}