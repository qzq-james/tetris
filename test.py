import asyncio

async def task1():
    print('A')
    j = 0
    
    print('wait')    
    await asyncio.sleep(1)

    # task = asyncio.create_task(task2())
    print('C')
    await asyncio.sleep(1)
    # print('C')
    # await asyncio.sleep(1)
    # print('C')
    # await asyncio.sleep(1)
    # print('C')
    # await asyncio.sleep(1)
    # print('C')
    # await asyncio.sleep(1)


async def task2():    
    await asyncio.sleep(2)

    print('B')
    # i=0
    # while i < 5:
    #     print('D')    
    #     await asyncio.sleep(1)
    #     i+=1
    await asyncio.sleep(2)

    print('f')
    

async def main():
    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())
    print('hello1')

    await task_1      
    print('hello2')
  
    await task_2


    print('hello3')

    # await asyncio.gather(asyncio.create_task(task1()), asyncio.create_task(task2()))
    # print('hello3')


asyncio.run(main())