import time
from datetime import datetime
now = time.time()
# time fuction return second since 1970
# scientific notation with f"{x:.2e} .2-> two digits after the decimal point
# float format (now:4f) and using , (now:e) for more readable structure
print(f"Seconds since January 1, 1970: {now:,.4f} or {now:.2e} "
      "in scientific notation")

# datetime.fromtimestamp function is cast timestamp to the readable date time
dt = datetime.fromtimestamp(now)
# make more readable with strftime %b month %d day %Y year
print(dt.strftime("%b %d %Y"))
