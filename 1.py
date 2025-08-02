import asyncio


async def a(n):
    await asyncio.sleep(n)
    return n

async def t_asyncio():
    a1 = asyncio.create_task(a(1))
    a2 = await a(2)
    a3 = a(3)

    print(await a1)
    print(a2)
    print(await a3)


if __name__ == '__main__':
    asyncio.run(t_asyncio())