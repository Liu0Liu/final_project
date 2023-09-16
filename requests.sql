SELECT c.login,
       COUNT (o.track)
FROM "Couriers" AS c
JOIN "Orders" AS o ON o."courierId" = c.id
WHERE o."inDelivery" = TRUE
GROUP BY c.login
ORDER BY c.login ASC;

SELECT track,
       CASE
           WHEN "finished" = TRUE THEN '2'
           WHEN "cancelled" = TRUE THEN '-1'
           WHEN "inDelivery" = TRUE THEN '1'
           ELSE '0'
       END
FROM "Orders";