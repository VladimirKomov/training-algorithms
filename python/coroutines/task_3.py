import asyncio


async def producer(queue: asyncio.Queue):
    try:
        i = 0
        while True:
            await asyncio.sleep(1)
            i += 1
            await queue.put(i)
            print(f"Producing {i}")
    except asyncio.CancelledError:
        raise



async def consumer(name: str, queue: asyncio.Queue):
    while True:
        item = await queue.get()
        print(f"Consuming {name}: got {item}")
        await asyncio.sleep(2)
        queue.task_done()

async def main():
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queue))

    consumer_tasks = {
        asyncio.create_task(consumer("consumer1", queue)),
        asyncio.create_task(consumer("consumer2", queue)),
        asyncio.create_task(consumer("consumer3", queue))
    }

    await asyncio.sleep(10)

    producer_task.cancel()

    try:
        await producer_task
    except asyncio.CancelledError:
        print("Producer cancelled")
    finally:
        await queue.join()

    for task in consumer_tasks:
        task.cancel()

    await asyncio.gather(*consumer_tasks, return_exceptions=True)


if __name__ == '__main__':
    asyncio.run(main())





