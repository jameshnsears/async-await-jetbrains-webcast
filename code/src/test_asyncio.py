# https://docs.python.org/3.6/library/asyncio.html

# single-threaded, serial multiplexing of coroutines
import asyncio

from colorama import Fore


# coroutine == "async def"
async def multiply_number_by_two(number: int, color: Fore):
    # simulate something blocking
    # use await to let event loop move on to next coroutine (which is asyncio.sleep!)
    await asyncio.sleep(number)
    print(color + f'{number * 2:d}', flush=True)


async def place_futures_on_event_loop():
    # "task" / "future" = a chunk of code that not immediately placed on event loop
    task1 = asyncio.ensure_future(multiply_number_by_two(4, Fore.BLUE))
    task2 = asyncio.get_event_loop().create_task(multiply_number_by_two(3, Fore.BLUE))
    await asyncio.sleep(2)

    # place tasts on event loop
    await asyncio.wait([task1, task2])


"""
inside a coroutine we can also use on blocks of code "async with" - an async context manager
"""

event_loop = asyncio.get_event_loop()

coroutines = [multiply_number_by_two(2, Fore.RED),
              multiply_number_by_two(1, Fore.RED)]
event_loop.run_until_complete(asyncio.gather(*coroutines))  # immediate execution of coroutines

event_loop.run_until_complete(asyncio.ensure_future(place_futures_on_event_loop()))

event_loop.close()

# 3.7 syntax simplified above - i.e.
# asyncio.run(coroutines)
