import asyncio
import random

sem = asyncio.Semaphore(5)

async def worker(job_id: int):
    async with sem:
        print(f"Task {job_id} started")
        await asyncio.sleep(random.uniform(0.5, 2))
        print(f"Task {job_id} finished")
        return job_id

async def scheduler(jobs):
    results = []
    pending = set()

    for job in jobs[:5]:
        pending.add(asyncio.create_task(worker(job)))

    for job in jobs[5:]:
        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

        for d in done:
            results.append(d.result())

        pending.add(asyncio.create_task(worker(job)))

    results.extend(await asyncio.gather(*pending))
    return results

async def main():
    jobs = list(range(20))
    results = await scheduler(jobs)
    print("All done:", results)

if __name__ == '__main__':
    asyncio.run(main())
