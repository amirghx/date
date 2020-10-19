from datetime import timedelta
from khayyam import JalaliDate, JalaliDatetime
now = JalaliDatetime(1399, 4, 31, 16, 17, 31, 374398)
print(now + timedelta(seconds=3600))