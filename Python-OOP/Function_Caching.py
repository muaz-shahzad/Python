from functools import lru_cache
import time


# Use tab krna jab limited values k liye fucntuon run krna h r result confirm h


@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*5



print(fx(2))
print("Done for 2")
print(fx(4))
print("Done for 4")
print(fx(6))
print("Done for 6")

# When again same value computation function take result from caching memory and work fast
print(fx(2))
print("Done for 2")
print(fx(4))
print("Done for 4")
print(fx(6))
print("Done for 6")
# Here function again take time for computation
print(fx(8))
print("Done for 8")



