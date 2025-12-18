-- База данных для учёта студентов, преподавателей, предметов и оценок (Вариант 1)


CREATE DATABASE IF NOT EXISTS UniversityDB;
USE UniversityDB;

-- Таблица Преподаватели
CREATE TABLE Teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    birth_date DATE,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    hire_date DATE NOT NULL
);

-- Таблица Студенты
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    birth_date DATE,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    enrollment_date DATE NOT NULL,
    group_name VARCHAR(20) NOT NULL
);

-- Таблица Предметы
CREATE TABLE Subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL UNIQUE,
    is_math_related BOOLEAN DEFAULT FALSE
);

-- Таблица Курсы (преподавание предмета в году/семестре)
CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_id INT NOT NULL,
    teacher_id INT NOT NULL,
    academic_year VARCHAR(9) NOT NULL,
    semester INT CHECK (semester IN (1, 2)),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id),
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

-- Таблица Связи студент-курс
CREATE TABLE StudentCourses (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE
);

-- Таблица Оценки
CREATE TABLE Grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    teacher_id INT NOT NULL,
    grade INT CHECK (grade BETWEEN 1 AND 5),
    grade_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

CREATE INDEX idx_student ON Grades(student_id);
CREATE INDEX idx_course ON Grades(course_id);