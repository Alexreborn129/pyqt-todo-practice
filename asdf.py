from datetime import datetime, date

today = date.today()
# print(f"{today.day}, {today.month}")
due = date(2026, 2, 1) # year, month, day

print(abs(due - today))