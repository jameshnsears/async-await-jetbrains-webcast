# https://docs.python.org/3.6/library/asyncio.html

# single-threaded, serial multiplexing of coroutines = parallelism without thread's
# in a "select" like way
# based on generator (yield / 3.4 "yield from") capabilities, that allow pausing and resuming of a function

import asyncio

from colorama import Fore


# coroutine == "async def"
# allow execution to be suspended and resumed
async def multiply_number_by_two(number: int, color: Fore):
    print(color + f'{number:d}', flush=True)

    # simulate something blocking
    # use await to let event loop move on to next coroutine (which is asyncio.sleep!)
    await asyncio.sleep(number)
    print(color + f'{number} * 2 = {number * 2:d}', flush=True)
    return number * 2


# "Future's" are objects that have the __await__() method implemented
# also has a callback API (that allows cancellation amongst other things)
# https://docs.python.org/3/library/asyncio-task.html

# "Tasks" are special Futures, which wrap coroutines, and not immediately placed on event loop
async def place_tasks_on_event_loop():
    # both API's do same thing in 3.6, maybe API improved in 3.7?
    task1 = asyncio.ensure_future(multiply_number_by_two(4, Fore.BLUE))
    task2 = asyncio.get_event_loop().create_task(multiply_number_by_two(3, Fore.BLUE))
    await asyncio.sleep(2)

    # place tasks on event loop & wait for them to complete
    await asyncio.wait([task1, task2])

    print(task1.result())
    print(task2.result())


"""
inside a coroutine we can also use on blocks of code "async with" - an async context manager
"""

event_loop = asyncio.get_event_loop()

# LIFO, in list but the ".sleep" shows how "yield from" outcome :-)
coroutines = [multiply_number_by_two(1, Fore.RED),
              multiply_number_by_two(2, Fore.RED)]
event_loop.run_until_complete(asyncio.gather(*coroutines))  # immediate execution of coroutines

event_loop.run_until_complete(asyncio.ensure_future(place_tasks_on_event_loop()))

event_loop.close()

# 3.7 syntax simplified above - i.e.
# asyncio.run(coroutines)


"""
Interesting side note: https://docs.python.org/3/library/selectors.html
"""