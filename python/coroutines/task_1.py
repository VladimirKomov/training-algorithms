import asyncio
from dataclasses import dataclass

import time


@dataclass
class Task():
    name: str
    delay: float

task_1 = Task("Task 1", 0.5)
task_2 = Task("Task 2", 1.0)
task_3 = Task("Task 3", 2.0)


async def start_task(task: Task) -> str:
    print(f"{task.name} started with delay {task.delay}")
    await asyncio.sleep(task.delay)
    print(f"{task.name} finished with delay {task.delay}")
    return f"{task.name}"

async def run_with_await():
    time_start = time.time()
    r1 = await start_task(task_1)
    r2 = await start_task(task_2)
    r3 = await start_task(task_3)
    time_end = time.time()
    duration = time_end - time_start
    print(f"Results: {r1}/{r2}/{r3} for {duration} seconds")

async def run_with_gather():
    time_start = time.time()
    results = await asyncio.gather(start_task(task_1), start_task(task_2), start_task(task_3))
    time_end = time.time()
    duration = time_end - time_start
    print(f"Results: {results} for {duration} seconds")


async def run_with_wait():
    time_start = time.time()
    tasks = {
        asyncio.create_task(start_task(task_1)),
        asyncio.create_task(start_task(task_2)),
        asyncio.create_task(start_task(task_3)),
    }

    while tasks:

        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        for d in done:
            time_end = time.time()
            duration = time_end - time_start
            print(f"Results: {d.result()} for {duration} seconds")






def main():
    # print("Awaiting...")
    # asyncio.run(run_with_await())
    # print("Gathering...")
    # asyncio.run(run_with_gather())
    print("Waiting...")
    asyncio.run(run_with_wait())

if __name__ == "__main__":
    main()



