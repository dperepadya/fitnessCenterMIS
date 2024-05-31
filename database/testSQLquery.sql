SELECT clients.id AS client_id, name AS client_name
FROM credentials JOIN clients ON credentials.client_id = clients.id
WHERE credentials.login = 'larry123' AND credentials.password = '12345'