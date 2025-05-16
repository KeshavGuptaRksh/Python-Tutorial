def count_up_to(max_num):
    current = 0
    def counter():
        nonlocal current
        current += 1
        return current
    return iter(counter, max_num + 1)

# Usage
my_iterator = count_up_to(5)
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(list(my_iterator))  # [3, 4, 5]