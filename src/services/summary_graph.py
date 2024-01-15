from datetime import datetime, timedelta
from matplotlib import pyplot as plt


def summary_display(weeks):
    weeks.sort(key=lambda x: datetime.strptime(x.monday, "%Y-%m-%d"))

    last_10_weeks = weeks[-10:]

    fechas = [(datetime.strptime(week.monday, "%Y-%m-%d") +
               timedelta(days=7)).strftime("%Y-%m-%d") for week in last_10_weeks]
    horas_trabajadas = [week.get_total_hours() for week in last_10_weeks]
    colores = ['red' if hour < 10 else 'green' for hour in horas_trabajadas]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(fechas, horas_trabajadas,
                   color=colores, label='Horas trabajadas')

    plt.axhline(y=10, color='r', linestyle='--', label='_nolegend_')

    for bar, week in zip(bars, last_10_weeks):
        height = bar.get_height()
        formatted_total = week.get_formatted_total()
        plt.text(bar.get_x() + bar.get_width() / 2, height,
                 formatted_total, ha='center', va='bottom')

    plt.title('Resumen semanal')
    plt.ylabel('Horas trabajadas')
    plt.xticks(rotation=45, ha='right')
    plt.ylim(0, 12)
    plt.legend()

    plt.tight_layout()
    plt.show(block=False)
