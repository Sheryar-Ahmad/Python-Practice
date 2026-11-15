# for each loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# for in loop
for i in range(5):
    print(i)

# for loop with index
for index, fruit in enumerate(fruits):
    print(index, fruit)
    
# for loop with dictionary
scores = {"Alice": 88, "Bob": 92}
for name, score in scores.items():
    print(name, score)

# while loop
count = 1
while count <= 3:
    print(count)
    count += 1

# nested loop
colors = ["red", "blue"]
shapes = ["circle", "square"]
for color in colors:
    for shape in shapes:
        print(color, shape)
