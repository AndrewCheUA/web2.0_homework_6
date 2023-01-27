SELECT students.full_name, g.group_name 
FROM students
JOIN st_groups as g ON g.id = students.group_id 
WHERE g.group_name = "group 2";