import time


def usingWhile():
    i = 0
    while i < 10:
        i = i + 1
        print(i)


def usingFor():
    for i in range(10):
        print(i)


init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
print(time.time() - init)
print(t1)

#for wait a program to execute a next line
time.sleep(4)
print("Printed After 3 seconds")

# Get local time
t = time.localtime()
formated_time = time.strftime("%y-%m-%d %H:%M:%S",t)
print(formated_time)