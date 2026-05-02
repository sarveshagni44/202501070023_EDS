from datetime import date
from datetime import datetime
d1 = input() 
d2 = input() 
a = datetime.strptime(d1, "%Y-%m-%d")
b = datetime.strptime(d2, "%Y-%m-%d")

print((b - a).days)
