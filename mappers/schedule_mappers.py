from db_models.schedule import Schedule as ScheduleModel
from models.schedule import Schedule as Schedule


def schedule_to_scheduledb(schedule):
    if schedule is None:
        return None
    return ScheduleModel(
            date=schedule.date,
            start_time=schedule.start_time,
            end_time=schedule.end_time,
            trainer_id=schedule.trainer_id
        )


def scheduledb_to_schedule(schedule):
    if schedule is None:
        return None
    return Schedule(
        date=schedule.date,
        start_time=schedule.start_time,
        end_time=schedule.end_time,
        trainer_id=schedule.trainer_id
        )
