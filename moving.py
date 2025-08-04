import asyncio

from pynput import keyboard

Pause_key = False

def set_global_var(var):
    global Pause_key
    Pause_key = var


def move_left(rb_col):
    rb_col -= 1


def on_press(key):
    try:
        if key == keyboard.Key.left:
            print('left')
            # move_left(rb_col)
        if key == keyboard.Key.right:
            print('right')
    except Exception as e:
        print(f'Worng: {e}')


def on_release(key):
    global Pause_key
    if key == keyboard.Key.esc or Pause_key:
        return False
    

async def sleep():
    await asyncio.sleep(2)
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


if __name__ == '__main__':
    asyncio.run(block_lr())
