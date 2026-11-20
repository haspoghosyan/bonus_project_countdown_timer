import time

user_time = input("Insert time to count down (h:m:s): ")

hours, minutes, seconds = user_time.split(":")

hours = int(hours)
minutes = int(minutes)
seconds = int(seconds)

total_seconds = hours * 3600 + minutes * 60 + seconds

while total_seconds >= 0:
    hours = total_seconds // 3600
    remainder = total_seconds % 3600

    minutes = remainder // 60
    seconds = remainder % 60

    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    time.sleep(1)

    total_seconds -= 1

print("Countdown finished!")


