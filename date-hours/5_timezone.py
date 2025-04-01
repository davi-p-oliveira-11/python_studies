from datetime import datetime, timedelta, timezone

date_oslo = datetime.now(timezone(timedelta(hours=2)))
date_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(date_oslo)
print(date_sao_paulo)