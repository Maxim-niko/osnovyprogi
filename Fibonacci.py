def fibonacci(x):
    if x in (1, 2):
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)
