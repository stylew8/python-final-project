import React from 'react';
import '../styles/studentSubjectDetailed.css';

const StudentSubjectDetailed = ({ subject }) => {
  // Normally, we'd fetch this data based on the subject ID
  // For this example, we'll use mock data
  const subjectData = {
    code: "P175B162",
    name: "Programavimo kalba Python",
    credits: 6,
    hours: 160,
    lecturer: "Jonas Jonaitis",
    finalGrade: null,
    tasks: [
      { name: "Laboratorinis darbas 1", weight: 10, grade: 9 },
      { name: "Laboratorinis darbas 2", weight: 10, grade: null },
      { name: "Laboratorinis darbas 3", weight: 10, grade: null },
      { name: "Laboratorinis darbas 4", weight: 10, grade: null },
      { name: "Egzaminas", weight: 60, grade: null },
    ]
  };

  const calculateTotalGrade = () => {
    let total = 0;
    let totalWeight = 0;
    subjectData.tasks.forEach(task => {
      if (task.grade !== null) {
        total += task.grade * task.weight;
        totalWeight += task.weight;
      }
    });
    return totalWeight > 0 ? (total / totalWeight).toFixed(2) : "N/A";
  };

  return (
    <div className="student-subject-detailed-container">
      <div className="student-subject-detailed-header">
        <h1 className="student-subject-detailed-title">{subjectData.name}</h1>
        <p className="student-subject-detailed-code">{subjectData.code}</p>
      </div>
      <div className="student-subject-detailed-info">
        <p>Kreditai: {subjectData.credits}</p>
        <p>Valandos: {subjectData.hours}</p>
        <p>Dėstytojas: {subjectData.lecturer}</p>
      </div>
      <div className="student-subject-detailed-grades">
        <h2>Įvertinimai</h2>
        <table className="student-subject-detailed-table">
          <thead>
            <tr>
              <th>Užduotis</th>
              <th>Svoris</th>
              <th>Įvertinimas</th>
            </tr>
          </thead>
          <tbody>
            {subjectData.tasks.map((task, index) => (
              <tr key={index}>
                <td>{task.name}</td>
                <td>{task.weight}%</td>
                <td>{task.grade !== null ? task.grade : '-'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="student-subject-detailed-final-grade">
        <p>Galutinis įvertinimas: {subjectData.finalGrade || calculateTotalGrade()}</p>
      </div>
    </div>
  );
};

export default StudentSubjectDetailed;

