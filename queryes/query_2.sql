SELECT s.full_name, ROUND(AVG(grade),2), su.subject
FROM grades as g
JOIN students as s ON g.student_id = s.id
JOIN subjects as su ON g.subject_id = su.id
WHERE su.subject = "History"
GROUP BY s.full_name
ORDER BY ROUND(AVG(g.grade),2) DESC LIMIT 1;