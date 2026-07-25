import time
count = int(input("entre the time in seconds"))
for i in range (count,0,-1):
    seconds = i % 60
    minutes = (i % 3600) // 60
    hours = i // 3600
    print (f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    count -=1

print("times up")