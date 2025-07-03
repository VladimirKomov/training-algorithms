import asyncio
from functools import wraps
from time import sleep, time


def log_it(file_name="log.txt"):
    def log_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time() #time.perf_counter()
            func_result = func(*args, **kwargs)
            end_time = time()
            duration = end_time - start_time
            with open(file_name, "a") as f:
                f.write(f"Function {func.__name__} takes time {duration}\n")
            return func_result

        return wrapper

    return log_decorator


def async_logger(file_name="log.txt"):
    def decorator(func):
        if not asyncio.iscoroutinefunction(func):
            raise TypeError("Этот декоратор можно применять только к async def функциям")

        @wraps(func)
        async def wrapper(*args, **kwargs):
            start = time()
            try:
                result = await func(*args, **kwargs)
                return result
            finally:
                duration = time() - start
                log_entry = f"{func.__name__} executed in {duration:.4f}s\n"
                async with aiofiles.open(file_name, "a") as f:
                    await f.write(log_entry)
        return wrapper
    return decorator


# @log_it("lod_2.txt")
def do_something():
    sleep(1)
    print("Everything is ok")


# do_something()
inner_decorator = log_it("lod_2.txt")
print(inner_decorator)
outer_decorator = inner_decorator(do_something)
print(outer_decorator)
outer_decorator()