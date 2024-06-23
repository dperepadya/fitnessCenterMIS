from db_models.service import Service as ServiceModel
from models.service import Service as Service
from utils.converters import safe_assign


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


def existing_service_to_servicedb(existing_service, service):
    if existing_service is None or service is None:
        return None
    safe_assign(existing_service, 'id', service.id)
    safe_assign(existing_service, 'name', service.name)
    safe_assign(existing_service, 'age', service.age)
    safe_assign(existing_service, 'gender', service.gender)
    safe_assign(existing_service, 'fitness_center_id', service.fitness_center_id)


