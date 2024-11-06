def minutes_to_hours(minutes):
    hours = minutes // 60
    minutes_remaining = minutes % 60
    return hours, minutes_remaining


def hours_to_minutes(hours, additional_minutes):
    total_minutes = (hours * 60) + additional_minutes
    return total_minutes


minutes = int(input("\nDigite o total de minutos: "))
horas, minutes_remaining = minutes_to_hours(minutes)
print(
    f"{minutes} minutos corresponde a {horas} hora(s) e {minutes_remaining} minuto(s)."
)


hours = int(input("\nDigite o número de horas: "))
additional_minutes = int(input("\nDigite o número de minutos: "))
total_minutes = hours_to_minutes(hours, additional_minutes)
print(
    f"{hours} hora(s) e {additional_minutes} minutos totalizam {total_minutes} minutos."
)
