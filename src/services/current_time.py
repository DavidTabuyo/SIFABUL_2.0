import arrow
import requests


def get_current_time(self) -> tuple[str, str, str]:
    timestamp = arrow.get(requests.get('http://worldtimeapi.org/api/timezone/Europe/Madrid').json()['datetime'])
    monday = timestamp.floor('week').format('YYYY-MM-DD')
    date = timestamp.format('YYYY-MM-DD')
    time = timestamp.format('HH:mm:ss')
    datetime= timestamp.format('YYYY-MM-DD HH:mm:ss')
    return (monday, date, time, datetime)
