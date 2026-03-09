from datetime import datetime

record_date = datetime(2026, 1, 14, 14, 53)

print(record_date.strftime("%Y/%m/%d %H:%M:%S"))
print(record_date.strftime("%y/%B/%d %H:%M:%S %p"))
print(record_date.strftime("%a, %Y %b %d"))
print(record_date.strftime("%A, %Y %B %d"))
print(record_date.strftime("Día de la semana: %w"))
print(record_date.strftime("Día del año: %j"))
print(record_date.strftime("Número de semana en el año: %W"))
