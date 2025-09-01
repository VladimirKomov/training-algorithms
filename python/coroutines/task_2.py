import asyncio
import time


async def worker():
    count = 0
    try:
        while True:
            count += 1
            await asyncio.sleep(1)
            print(f'{count} task done')
    except asyncio.CancelledError:
        print(f'{count} tasks cancelled')
    finally:
        await asyncio.sleep(1)
        print(f'Stopping {count} tasks')

async def main():
    task = asyncio.create_task(worker())
    time_start = time.time()
    while (time.time() - time_start) < 5:
        await asyncio.sleep(0.1)

    task.cancel()
    await task

if __name__ == '__main__':
    asyncio.run(main())