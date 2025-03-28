import time

# Get current hour, minute, second as integers
hour = int(time.strftime("%H"))
minute = int(time.strftime("%M"))
second = int(time.strftime("%S"))

#Current time =>
print(f"Current time is = {hour}:{minute}:{second}")

if 0 <= hour < 6:
    print("Good Night...!")
elif 6 <= hour < 12:
    print("Good Morning..!")
elif 12 <= hour < 17:
    print("Good AfterNoon..!")
else:
    print("Good Evening..!")    