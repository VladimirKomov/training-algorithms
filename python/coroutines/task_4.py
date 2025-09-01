import asyncio
import random
import signal

shutdown_event = asyncio.Event()

def handle_signal(sig, frame=None):
    print("[Signal] Shutdown signal received signal {}".format(sig))
    shutdown_event.set()


async def worker(name: str, queue: asyncio.Queue):
    while not shutdown_event.is_set() or not queue.empty():
        try:
            item = await asyncio.wait_for(queue.get(), timeout=2)
        except asyncio.TimeoutError:
            print("[Worker] Timeout received")
            continue
        print(f"[Worker] {name} working... processing {item}")
        await asyncio.sleep(random.uniform(1, 1.5))
        queue.task_done()
    print("[Worker] Shutdown signal received")

async def producer(queue):
    count = 0
    while not shutdown_event.is_set():
        count += 1
        await asyncio.sleep(1)
        await queue.put(count)
        print("[Put task] {}".format(count))
    print("[Producer] Shutdown signal received")


async def main():
    queue = asyncio.Queue()

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)


    producer_task = asyncio.create_task(producer(queue))
    workers = [asyncio.create_task(worker(f"worker {i}", queue)) for i in range(3)]

    await asyncio.gather(producer_task)
    await queue.join()
    shutdown_event.set()
    await asyncio.gather(*workers)


if __name__ == "__main__":
    asyncio.run(main())

