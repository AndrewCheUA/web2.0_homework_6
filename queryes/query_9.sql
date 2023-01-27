SELECT students.full_name, subjects.subject
FROM grades 
JOIN students on students.id = student_id
JOIN subjects on subjects.id = subject_id
WHERE student_id = 15