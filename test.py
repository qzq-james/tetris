import asyncio
import time

async def task1():
    print("Task 1 started")
    time.sleep(10)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def main():
    # Schedule tasks concurrently
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    await t1
    await t2

asyncio.run(main())
# Output:
# Task 1 started
# Task 2 started
# Task 2 finished
# Task 1 finished