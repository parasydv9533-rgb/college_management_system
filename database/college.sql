
create database college_db3;
use college_db3;

-- =========================
-- DEPARTMENTS
-- =========================
CREATE TABLE departments(
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100)
);

-- =========================
-- STUDENTS
-- =========================
CREATE TABLE students(
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    gender ENUM('Male','Female','Other'),
    dob DATE,
    phone VARCHAR(15),
    email VARCHAR(100),
    address VARCHAR(255),
    department_id INT,
    FOREIGN KEY(department_id)
    REFERENCES departments(department_id)
);

-- =========================
-- TEACHERS
-- =========================
CREATE TABLE teachers(
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender ENUM('Male','Female','Other'),
    phone VARCHAR(15),
    email VARCHAR(100),
    qualification VARCHAR(100),
    salary DECIMAL(10,2),
    department_id INT,
    FOREIGN KEY(department_id)
    REFERENCES departments(department_id)
);

-- =========================
-- COURSES
-- =========================
CREATE TABLE courses(
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100),
    duration VARCHAR(50),
    total_fee DECIMAL(10,2)
);

-- =========================
-- SUBJECTS
-- =========================
CREATE TABLE subjects(
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(100),
    course_id INT,
    semester VARCHAR(20),
    FOREIGN KEY(course_id)
    REFERENCES courses(course_id)
);

-- =========================
-- ENROLLMENTS
-- =========================
CREATE TABLE enrollments(
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    admission_date DATE,
    status VARCHAR(30),
    FOREIGN KEY(student_id)
    REFERENCES students(student_id),
    FOREIGN KEY(course_id)
    REFERENCES courses(course_id)
);

-- =========================
-- ATTENDANCE
-- =========================
CREATE TABLE attendance(
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    attendance_date DATE,
    status ENUM('Present','Absent'),
    FOREIGN KEY(student_id)
    REFERENCES students(student_id)
);

-- =========================
-- FEES
-- =========================
CREATE TABLE fees(
    fee_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    total_fee DECIMAL(10,2),
    paid_fee DECIMAL(10,2),
    remaining_fee DECIMAL(10,2),
    payment_date DATE,
    status ENUM('Paid','Pending'),
    FOREIGN KEY(student_id)
    REFERENCES students(student_id)
    );

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role ENUM('Admin','Teacher','Staff') NOT NULL DEFAULT 'Admin'
);

 
 
 



 





