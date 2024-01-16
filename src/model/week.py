class Week:
    def __init__(self, worker_id: str, monday: str, total: int):
        self.worker_id = worker_id
        self.monday = monday
        self.total = total

    def is_above_threshold(self) -> bool:
        if self.total < 10:
            return True
        return False

    def get_total_hours(self) -> float:
        return self.total/3600

    def get_formatted_total(self):
        hours, remainder = divmod(self.total, 3600)
        minutes = remainder // 60
        formatted_hours = f"{int(hours):02d} h"
        formatted_minutes = f"{int(minutes):02d} min" if minutes > 0 else ""
        return f"{formatted_hours} {formatted_minutes}"
