SELECT sub.subject, grade, st.group_name, date_stamp
FROM grades 
JOIN st_groups as st ON st.id = student_id
JOIN subjects as sub ON sub.id = subject_id
WHERE sub.id = 2 and st.id  = 1 and date_stamp BETWEEN  '2023-03-15' AND '2023-12-28'