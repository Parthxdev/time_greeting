#Input Current time =>
time = int(input("Enter a time : "))

if 0 <= time < 6:
    print("Good Night...!")
elif 6 <= time < 12:
    print("Good Morning..!")
elif 12 <= time < 17:
    print("Good AfterNoon..!")
else:
    print("Good Evening..!")    