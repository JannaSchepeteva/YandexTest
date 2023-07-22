1 задание:

SELECT "Couriers".login, COUNT("Orders".id) AS orders_count
FROM "Couriers" INNER JOIN "Orders" ON "Couriers".id = "Orders"."courierId"
WHERE "Orders"."inDelivery" = true
GROUP BY "Couriers".login;


2 задание:

SELECT track,
CASE WHEN finished=true THEN 2
WHEN cancelled=true THEN -1
WHEN "inDelivery"=true THEN 1
ELSE 0
END AS order_status
FROM "Orders";


