import random
import my_module

random_number = random.randint(1,100)
print(random_number)

random_num_0_to_1 = random.random()
print(random_num_0_to_1)

randon_float = random.uniform(1,10)
print(randon_float)

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 1:
    print("Tail")
else:
    print("Head")

print(my_module.PI)

