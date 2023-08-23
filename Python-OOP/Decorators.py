#
#
# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("THanks for your time ")
#     return mfx
#
# # @greet
# def Hello():
#     print("Hello World")
#
# @greet
# def person():
#     print("M Muaz Shahzad")
# # Hello()
# person()
#
# # greet(Hello)()
#
####################################################################################
#
# def function_ar(*arr) syntax for geeting argument as an tuple
# def function_ar(**arr) syntax for geeting argument as an Dictionary

def greet(fx):
    def mfx(*args):
        print("Good Morning")
        print(args)
        fx(*args)
        print("THanks for your time ")
    return mfx

@greet
def add(a,b):
    print(a+b)
@greet
def sub(a,b):
    print(a-b)

add(1,2)
sub(4,8)





