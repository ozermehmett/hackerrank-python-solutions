import calendar
month, day, year = input().split()
dayNum = calendar.weekday(int(year),int(month),int(day))
if dayNum == 0:
  print("MONDAY")
elif dayNum == 1:
  print("TUESDAY")
elif dayNum == 2:
  print("WEDNESDAY")
elif dayNum == 3:
  print("THURSDAY")
elif dayNum == 4:
  print("FRIDAY")
elif dayNum == 5:
  print("SATURDAY")
elif dayNum == 6:
  print("SUNDAY")
