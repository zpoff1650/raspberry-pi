import time


print(str(time.time()))
time.sleep(1)
print(str(time.time()))
time.sleep(1)
print(str(time.time()))


startTime=time.time()
while time.time()-startTime < 3:
    print("Not 3 seconds yet...")

print("DONE")


