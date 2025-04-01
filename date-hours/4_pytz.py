from datetime import datetime

import pytz

date = datetime.now(pytz.timezone("Europe/Oslo"))
date2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(date)
print(date2)