SELECT ROUND(AVG(grade),2), lecturers.full_name
FROM grades 
JOIN lecturers on lecturers.id = subject_id
WHERE lecturers.full_name = 'Tristan Price'