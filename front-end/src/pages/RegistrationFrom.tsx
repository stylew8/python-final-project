// import React, { useState } from 'react';
// import { Form, Button } from 'react-bootstrap';

// const RegistrationForm: React.FC = () => {
//     const [userType, setUserType] = useState('');

//     const handleSubmit = (e: React.FormEvent) => {
//         e.preventDefault();
//         // Handle form submission
//         console.log('Registration form submitted');
//     };

//     return (
//         <div>
//             <h2 className="mb-3">Registration</h2>
//             <Form onSubmit={handleSubmit}>
//                 <Form.Group className="mb-3" controlId="formUsername">
//                     <Form.Control type="text" placeholder="Username" required />
//                 </Form.Group>
//                 <Form.Group className="mb-3" controlId="formEmail">
//                     <Form.Control type="email" placeholder="Email" required />
//                 </Form.Group>
//                 <Form.Group className="mb-3" controlId="formPassword">
//                     <Form.Control type="password" placeholder="Password" required />
//                 </Form.Group>
//                 <Form.Group className="mb-3" controlId="formUserType">
//                     <Form.Select
//                         value={userType}
//                         onChange={(e) => setUserType(e.target.value)}
//                         required
//                     >
//                         <option value="">Select user type</option>
//                         <option value="student">Student</option>
//                         <option value="teacher">Teacher</option>
//                         <option value="admin">Administrator</option>
//                     </Form.Select>
//                 </Form.Group>
//                 {userType === 'student' && (
//                     <>
//                         <Form.Group className="mb-3" controlId="formStudentId">
//                             <Form.Control type="text" placeholder="Student ID" required />
//                         </Form.Group>
//                         <Form.Group className="mb-3" controlId="formMajor">
//                             <Form.Control type="text" placeholder="Major" required />
//                         </Form.Group>
//                     </>
//                 )}
//                 {userType === 'teacher' && (
//                     <>
//                         <Form.Group className="mb-3" controlId="formTeacherId">
//                             <Form.Control type="text" placeholder="Teacher ID" required />
//                         </Form.Group>
//                         <Form.Group className="mb-3" controlId="formDepartment">
//                             <Form.Control type="text" placeholder="Department" required />
//                         </Form.Group>
//                     </>
//                 )}
//                 {userType === 'admin' && (
//                     <>
//                         <Form.Group className="mb-3" controlId="formAdminId">
//                             <Form.Control type="text" placeholder="Admin ID" required />
//                         </Form.Group>
//                         <Form.Group className="mb-3" controlId="formDepartment">
//                             <Form.Control type="text" placeholder="Department" required />
//                         </Form.Group>
//                     </>
//                 )}
//                 <Button variant="primary" type="submit">
//                     Register
//                 </Button>
//             </Form>
//         </div>
//     );
// };

// export default RegistrationForm;

