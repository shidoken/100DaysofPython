import time


def c_time():
    current_time = time.time()
    return current_time


def speed_calc_decorator(function):
    def wrapper_function():
        # Do something before
        function()
        function_name = function.__name__
        time_1 = c_time()
        function()
        time_2 = c_time()
        difference_time = float(time_2) - float(time_1)
        print(f"{function_name} run speed: {difference_time}s")
        # Do something after
    return wrapper_function


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
