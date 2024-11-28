import React from 'react';
import '../styles/studentView.css';

const firstSemester = [
  { code: "S180B056", name: "Ekonomika", credits: "1", form: "L", hours: "3", status: "Peržiūrėti" },
  { code: "P000B201", name: "Programų sistemų inžinerija", credits: "1", form: "L", hours: "3", status: "Peržiūrėti" },
  { code: "P175B132", name: "Programų sistemų testavimas", credits: "1", form: "L", hours: "3", status: "Peržiūrėti" },
  { code: "P175B020", name: "Interneto svetainių serverio dalies kūrimas", credits: "1", form: "L", hours: "6", status: "Peržiūrėti" },
  { code: "P175B023", name: "Interneto svetainių kliento dalies kūrimas", credits: "1", form: "L", hours: "6", status: "Peržiūrėti" },
  { code: "P175B162", name: "Programavimo kalba Python", credits: "1", form: "L", hours: "3", status: "Peržiūrėti" },
  { code: "P175B202", name: "Duomenų analitika", credits: "1", form: "L", hours: "3", status: "Peržiūrėti" },
];

const secondSemester = [
  { code: "P000B233", name: "Programinės įrangos kūrimo valdymas", credits: "1", form: "L", hours: "3", status: "Peržiūrėti" },
  { code: "P176B001", name: "Intelektika", credits: "1", form: "L", hours: "3", status: "Peržiūrėti" },
  { code: "P000B270", name: "Profesinė praktika", credits: "1", form: "L", hours: "12", status: "Peržiūrėti" },
  { code: "P175B021", name: "Saityno saugumas", credits: "1", form: "L", hours: "3", status: "Peržiūrėti" },
  { code: "P175B138", name: "Svetainių optimizacija paieškos sistemoms", credits: "1", form: "L", hours: "3", status: "Peržiūrėti" },
  { code: "P175B160", name: "Programavimo kalba C#", credits: "1", form: "L", hours: "3", status: "Peržiūrėti" },
  { code: "P175B203", name: "React JS karkasas", credits: "1", form: "L", hours: "3", status: "Peržiūrėti" },
];

const SemesterTable = ({ courses }) => (
  <table className="student-view-table">
    <thead className="student-view-table-header">
      <tr>
        <th className="student-view-table-header-cell">Dalyko/modulio kodas ir pavadinimas</th>
        <th className="student-view-table-header-cell">Forma, dėstomoji kalba, kreditų sk.</th>
        <th className="student-view-table-header-cell">Įskaitos požymis</th>
        <th className="student-view-table-header-cell">Data</th>
        <th className="s tudent-view-table-header-cell">Tarpiniai įvertinimai</th>
      </tr>
    </thead>
    <tbody>
      {courses.map((course) => (
        <tr key={course.code} className="student-view-table-row">
          <td className="student-view-table-cell">{course.code} {course.name}</td>
          <td className="student-view-table-cell">{course.credits} {course.form}</td>
          <td className="student-view-table-cell">{course.hours}</td>
          <td className="student-view-table-cell"></td>
          <td className="student-view-table-cell">
            <a className="student-view-button" href='/studentSubjectDetailed'>{course.status}</a>
          </td>
        </tr>
      ))}
    </tbody>
  </table>
);

const StudentView = () => {
  return (
    <div className="student-view-container">
      <div className="student-view-card">
        <div className="student-view-card-header">
          <h1 className="student-view-title">Individualus studijų planas</h1>
          <p className="student-view-info-text">51831, Vardas Pavardė</p>
          <p className="student-view-info-text">Elektronikos ir informatikos fakultetas</p>
          <p className="student-view-info-text">Studijų programa: PI-22-ND, Programų sistemos</p>
          <p className="student-view-info-text">Akademinė grupė: PI22B</p>
          <p className="student-view-info-text">2024 / 2025 m. m.</p>
        </div>
      </div>

      <div className="student-view-card">
        <div className="student-view-card-header">
          <h2 className="student-view-semester-title">Rudens semestras (05)</h2>
        </div>
        <SemesterTable courses={firstSemester} />
        <div className="student-view-card-header">
          <p className="student-view-summary-text">Studijų plano semestro apimtis: 27 kr.</p>
          <p className="student-view-summary-text">Atsiskaityta: 0 kr.</p>
        </div>
      </div>

      <div className="student-view-card">
        <div className="student-view-card-header">
          <h2 className="student-view-semester-title">Pavasario semestras (06)</h2>
        </div>
        <SemesterTable courses={secondSemester} />
        <div className="student-view-card-header">
          <p className="student-view-summary-text">Studijų plano semestro apimtis: 23 kr.</p>
          <p className="student-view-summary-text">Atsiskaityta: 0 kr.</p>
        </div>
      </div>

      <p className="student-view-footer-text">
        Dėl plano keitimo ar pastebėtų netikslumų kreipkitės į savo fakulteto Studijų skyrių.
      </p>
    </div>
  );
};

export default StudentView;

