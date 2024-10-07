from datetime import datetime

from db_models.schedule import Schedule as ScheduleModel
from models.schedule import Schedule as Schedule


def schedule_to_scheduledb(schedule):
    if schedule is None:
        return None
    date_obj = datetime.strptime(schedule.date, '%Y-%m-%d').date()
    start_time_obj = datetime.strptime(schedule.start_time, '%H:%M').time()
    end_time_obj = datetime.strptime(schedule.end_time, '%H:%M').time()

    return ScheduleModel(
            date=date_obj,
            start_time=start_time_obj,
            end_time=end_time_obj,
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
