SELECT lecturers.full_name, s.subject
FROM lecturers
JOIN subjects as s ON s.lecturer_id = lecturers.id
WHERE lecturers.id = 2;