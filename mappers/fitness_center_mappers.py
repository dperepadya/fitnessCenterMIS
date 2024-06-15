from db_models.fitness_center import FitnessCenter as FcModel
from models.fitness_center import FitnessCenter as FitnessCenter


def fc_to_fcdb(fc):
    if fc is None:
        return None
    return FcModel(
        name=fc.name,
        address=fc.address,
        phone=fc.phone,
        email=fc.email
    )


def fc_to_fcdb(existing_fc, fc):
    if existing_fc is None or fc is None:
        return None
    existing_fc.name = fc.name,
    existing_fc.address = fc.address,
    existing_fc.phone = fc.phone,
    existing_fc.email = fc.email

    return existing_fc


def fcdb_to_fc(fc):
    if fc is None:
        return None
    return FitnessCenter(
        name=fc.name,
        address=fc.address,
        phone=fc.phone,
        email=fc.email
    )
