import asyncio

from pynput import keyboard

Pause_key = False

def on_press(key):
    try:
        if key == keyboard.Key.left:
            print('left')
        if key == keyboard.Key.right:
            print('right')
    except Exception as e:
        print(f'Worng: {e}')


def on_release(key):
    global Pause_key
    if key == keyboard.Key.esc or Pause_key:
        return False
    

async def sleep():
    print('here is in sleep func before sleep')
    await asyncio.sleep(2)
    print('after sleep')
    return True
    
    
async def moving():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        try: 
            while listener.running:
                await asyncio.sleep(0.1)    
        finally:
            listener.stop()


async def block_lr():
    global Pause_key
    task_sleep = asyncio.create_task(sleep())
    task_moving = asyncio.create_task(moving())

    pause = await task_sleep

    if pause:
        Pause_key = True

    await task_moving

    print('its over')


asyncio.run(block_lr())