#Using for small and simple function its not for complex functions

double = lambda x: x*2

# print(double(5))


# average  = lambda x,y: (x+y)/2
# print(average(2,2))

def appl(fx,value):
    return 6 + fx(value)
# fx(Value) is m fx = double function and value is 2  fx(2) = double(2)

print(appl(double,3))