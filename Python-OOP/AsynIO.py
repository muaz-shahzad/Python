import time
import asyncio


async def function1():
    await asyncio.sleep(1)
    print("Functoion 1")
    return "Muaz"


async def function2():
    await asyncio.sleep(1)
    print("Functoion 2")


async def function3():
    await asyncio.sleep(4)
    print("Functoion 3")


async def main():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
      )
    print(L)
# task = asyncio.create_task(function1())
    # # await function1()
    # await function2()
    # await function3()
asyncio.run(main())
