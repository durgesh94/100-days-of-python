import random

friends = ["Durgesh", "Vishal", "Amol", "Ram", "Raj", "Pravin"]

# Option 1
print(random.choice(friends))

# Option 2
idx = random.randint(0,5)
print(friends[idx])