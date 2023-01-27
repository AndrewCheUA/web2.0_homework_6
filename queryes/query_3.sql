SELECT ROUND(AVG(grade),2), st_groups.group_name, subjects.subject
FROM grades 
JOIN st_groups on st_groups.id = student_id
JOIN subjects on subjects.id = subject_id
WHERE st_groups.id = 3 and subjects.id = 1