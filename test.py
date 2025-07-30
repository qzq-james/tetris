import asyncio

async def func(time, num):
    print(f'No.{num} project start doing.')
    await asyncio.sleep(time)
    return {'task': f'{num} has finished.'}


async def main():
    task1 = asyncio.create_task(func(3, 1))
    task2 = asyncio.create_task(func(2, 2))

    result1 = await task1
    result2 = await task2
    task3 = asyncio.create_task(func(1, 3))
    result3 = await task3

    print(result1, result2, result3)


asyncio.run(main())