SELECT sub.subject, grade, st.group_name 
FROM grades 
JOIN st_groups as st ON st.id = student_id
JOIN subjects as sub ON sub.id = subject_id
WHERE sub.subject = 'Geometry' and st.group_name = 'group 3'