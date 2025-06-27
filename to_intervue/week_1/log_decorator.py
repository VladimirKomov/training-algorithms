from functools import wraps
from time import sleep, time


def log_it(file_name="log.txt"):
    def log_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time()
            func_result = func(*args, **kwargs)
            end_time = time()
            duration = end_time - start_time
            with open(file_name, "a") as f:
                f.write(f"Function {func.__name__} takes time {duration}\n")
            return func_result

        return wrapper

    return log_decorator


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