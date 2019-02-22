# https://docs.python.org/3.6/library/asyncio.html

# single-threaded, serial multiplexing of coroutines
import asyncio
from colorama import Fore


# coroutine == "async def"
async def multiply_number_by_two(number: int):
    # simulate something blocking
    # use await to let event loop move on to next coroutine (which is asyncio.sleep!)
    await asyncio.sleep(number)
    print(Fore.CYAN + f'{number * 2:d}', flush=True)


event_loop = asyncio.get_event_loop()

coroutines = [multiply_number_by_two(2),
              multiply_number_by_two(1)]

event_loop.run_until_complete(asyncio.gather(*coroutines))

event_loop.close()

# 3.7 syntax simplified above
# asyncio.run(coroutines)
