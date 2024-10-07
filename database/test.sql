SELECT
    services.name AS name,
    services.duration AS duration,
    services.price AS price,
    services.description AS description,
    services.max_attendees AS max_attendees
FROM
    trainer_services
JOIN
    services ON trainer_services.service_id = services.id
JOIN
    trainers ON trainer_services.trainer_id = trainers.id
WHERE
    trainers.id = 1
    AND trainers.fitness_center_id = 1
    AND services.fitness_center_id = 1