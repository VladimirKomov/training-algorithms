import asyncio
import random
import signal

shut_down_event = asyncio.Event()

def handle_signal(signum, frame):
    print("Signal received")
    shut_down_event.set()


async def producer(queue: asyncio.Queue):
    count = 0
    while not shut_down_event.is_set():
        await asyncio.sleep(0.5)
        await queue.put(count)
        count += 1
        print(f"Producing {count}")
    print("Shutdown signal received")


async def consumer(name: str, queue: asyncio.Queue):
    while not shut_down_event.is_set() or not queue.empty():
        try:
            item = await asyncio.wait_for(queue.get(), timeout=1)
        except asyncio.TimeoutError:
            print(f"Consumer {name} timed out")
            continue
        print(f"Consuming {name}: got {item}")
        await asyncio.sleep(random.uniform(0.5, 2))
        queue.task_done()
    print(f"Consumer {name} finished")

async def main():
    queue = asyncio.Queue()
    n_consumers = 5

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    producer_task = asyncio.create_task(producer(queue))
    consumer_tasks = [asyncio.create_task(consumer(f"Consumer {i}", queue)) for i in range(n_consumers)]

    await asyncio.gather(producer_task)
    await queue.join()
    await asyncio.gather(*consumer_tasks)

if __name__ == "__main__":
    asyncio.run(main())

