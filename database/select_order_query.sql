SELECT
    orders.id AS order_id,
    services.id AS service_id,
    services.name AS service_name,
    fitness_centers.id AS fitness_center_id,
    fitness_centers.name AS fitness_center_name,
    clients.id AS client_id,
    clients.name AS client_name
FROM 
    orders
JOIN 
    services ON orders.service_id = services.id
JOIN 
    fitness_centers ON services.fitness_center_id = fitness_centers.id
JOIN 
    clients ON orders.client_id = clients.id
WHERE 
    orders.id = 1

	