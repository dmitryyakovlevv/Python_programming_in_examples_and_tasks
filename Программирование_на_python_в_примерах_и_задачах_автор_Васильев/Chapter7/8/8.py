from datetime import datetime
md = datetime(2023, 2, 25, 13, 6, 0)
td = datetime.today()
delta = abs(td - md)
print(delta)