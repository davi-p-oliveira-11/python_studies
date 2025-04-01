from datetime import datetime

current_hour = datetime.now()
hour_date_str = "2025-10-20 10:20"
mask_ptbr = "%d/%m/%Y %a"
mask_en = "%Y-%m-%d %H:%M"

print(current_hour.strftime(mask_ptbr))

converted_date = datetime.strptime(hour_date_str, mask_en)
print(converted_date)
print(type(converted_date))