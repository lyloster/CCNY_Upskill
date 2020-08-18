hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
minsElapsed = (mins + dura)
mins = minsElapsed % 60
hour = (hour + (minsElapsed // 60)) % 12
print(hour, mins, sep = ':')
