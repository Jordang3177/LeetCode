SELECT DISTINCT
    p1.Email
FROM Person p1
JOIN Person p2
ON p1.Id != p2.Id and p1.Email = p2.Email