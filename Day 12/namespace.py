enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    # prints 2

increase_enemies()
print(f"enemies outside function: {enemies}")
# prints 1