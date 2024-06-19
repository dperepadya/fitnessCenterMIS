from db_models.service import Service as ServiceModel
from models.service import Service as Service


def servicedb_to_service(service):
    if service is None:
        return None
    service = Service(
        name=service.name,
        duration=service.duration,
        price=service.price,
        description=service.description,
        max_attendees=service.max_attendees
    )
    service.fitness_center_id = service.fitness_center_id
    return service


def service_to_servicedb(service):
    if service is None:
        return None
    return ServiceModel(
        name=service.name,
        duration=service.duration,
        price=service.price,
        description=service.description,
        max_attendees=service.max_attendees,
        fitness_center_id=service.fitness_center_id
    )


def service_to_servicedb(existing_service, service):
    if existing_service is None or service is None:
        return None
    existing_service.id = service.id
    existing_service.name = service.name,
    existing_service.age = service.age,
    existing_service.gender = service.gender,
    existing_service.fitness_center_id = service.fitness_center_id

