from datetime import date, datetime, timedelta, time

car_type = "M" # S, M, L
short_time = 30
medium_time = 45
large_time = 60
current_date = datetime.now()

if car_type == "S":
  estimated_date = current_date - timedelta(days=short_time)
  print(f"The car arrived: {current_date} and will be ready at {estimated_date}")
elif car_type == "M":
  estimated_date = current_date - timedelta(days=medium_time)
  print(f"The car arrived: {current_date} and will be ready at {estimated_date}")
else:
  estimated_date = current_date - timedelta(days=large_time)
  print(f"The car arrived: {current_date} and will be ready at {estimated_date}")

print(date.today() - timedelta(days=1))

result = datetime(2025, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(result.time())

print(datetime.now().date())