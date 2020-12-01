
numbers = []
with open('input.txt', 'r') as f:
    numbers = [int(x) for x in f.readlines()]

while len(numbers) > 0:
    x = numbers.pop()
    for y in numbers:
        for z in numbers:
          if x + y + z == 2020:
            print(f'{x} {y} {z} result: {x * y * z}')
            break

print('Done')