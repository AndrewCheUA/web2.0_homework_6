SELECT ROUND(AVG(g.grade), 2) as Average_grade, s.full_name as Student_name
FROM grades as g
JOIN students as s ON g.student_id = s.id
GROUP BY s.full_name
ORDER BY ROUND(AVG(g.grade), 2) DESC LIMIT 5;