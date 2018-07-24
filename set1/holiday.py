days=["Sunday","Monday","Tuesday","Wednesday"]
day=["Thursday","Saturday"]
s = input("Enter the day:")
for i in range(4):
  if (s == days[i]):
    print("yes")
    for i in range(2):
      if (s == day[i]):
        print("no")

