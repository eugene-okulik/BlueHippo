import sys


sys.set_int_max_str_digits(100_000)


def progression(limit=None):
    first = 0
    second = 1
    current_count = 0

    while True:
        if limit is not None and current_count >= limit:
            break

        yield second

        first, second = second, first + second
        current_count += 1


gen = progression()

count = 1
for number in gen:
    if count == 5:
        print(f"5 число: {number}")
    elif count == 200:
        print(f"200 число: {number}")
    elif count == 1000:
        print(f"1000 число: {number}")
    elif count == 100000:
        print(f"100000 число: {number}")
        break

    count += 1
