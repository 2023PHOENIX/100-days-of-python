# Modifiying Global scope

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function : {enemies}")


