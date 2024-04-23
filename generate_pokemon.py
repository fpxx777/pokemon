import random

def generate():
    num = random.random()
    if num < 0.33:
        num = 0
    elif num < 0.66:
        num = 1
    else:
        num = 2
    return num