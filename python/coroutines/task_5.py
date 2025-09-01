import asyncio
import math
import reprlib
from asyncio import Future
from concurrent.futures import ProcessPoolExecutor

import aiohttp


async def fetch_page(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            print(f"[Fetch] {response.status}: {url}: {text}")
            return text

def compute_factorial(n: int) -> int:
    print(f"[Compute factorial] Start for {n}")
    result = math.factorial(n)
    print(f"[Compute factorial] Finish for {n}")
    return result

async def main() -> None:
    url = "https://example.com"
    big_number = 50_000

    loop = asyncio.get_event_loop()

    with ProcessPoolExecutor() as executor:
        factorial_task: Future[int] = loop.run_in_executor(executor, compute_factorial, big_number)
        fetch_page_task: asyncio.Task[str] = asyncio.create_task(fetch_page(url))

        factorial, html = await asyncio.gather(factorial_task, fetch_page_task)

    digits = factorial.bit_length() // 3 + 1
    print(f"[Result] IO: {len(html)} chars, CPU: digits={digits}...")


if __name__ == "__main__":
    asyncio.run(main())