n = [1,2,3,4,5,6,7,8]

while p := len(n) > 0:
    print(n.pop(), end=" ")


foods = list()

while True:
    food = input("what food do you like?: ")
    if food == "quit":
        break
    foods.append(food)


while(food := input("what food do you like?: ") != 'quit'):
    foods.append(food)