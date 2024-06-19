from db_models.fitness_center import FitnessCenter as FcModel
from models.fitness_center import FitnessCenter as FitnessCenter
from utils.converters import safe_assign


def fc_to_fcdb(fc):
    if fc is None:
        return None
    return FcModel(
        name=fc.name,
        address=fc.address,
        phone=fc.phone,
        email=fc.email
    )


def existing_fc_to_fcdb(existing_fc, fc):
    if existing_fc is None or fc is None:
        return None
    safe_assign(existing_fc, 'name', fc.name)
    safe_assign(existing_fc, 'address', fc.address)
    safe_assign(existing_fc, 'phone', fc.phone)
    safe_assign(existing_fc, 'email', fc.email)


def fcdb_to_fc(fc):
    if fc is None:
        return None
    return FitnessCenter(
        name=fc.name,
        address=fc.address,
        phone=fc.phone,
        email=fc.email
    )
