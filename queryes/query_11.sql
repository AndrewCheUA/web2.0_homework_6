SELECT ROUND(AVG(grade),2), students.full_name, subjects.subject, lecturers.full_name 
FROM grades 
JOIN students on students.id = student_id
JOIN subjects on subjects.id = subject_id
JOIN lecturers on lecturers.id = subjects.id
where student_id = 15 and lecturers.id = 1