def my_genrator():
    for i in range(5):
        yield i             #yeild keyword generator return krta h r execution ko suspend krta h


gen = my_genrator()
# print(next(gen))

for j in gen:
    print(j)